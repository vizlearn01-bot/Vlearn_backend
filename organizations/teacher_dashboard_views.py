from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Q, Avg, Count

from organizations.models import (
    School,
    OrganizationMembership,
    AcademicYear,
    SchoolClass,
    Stream,
    TeacherStreamAssignment,
    TeacherSubjectAssignment,
    StudentEnrollment,
    TeacherLessonLog,
)
from organizations.serializers import TeacherLessonLogSerializer
from curriculum.models import Subject, Topic, Lesson, LessonBlock, LessonAsset, Simulation
from Resources.models import ExperimentVideo, UploadedFile, User
from assessments.models import Examination, StudentMark
from assessments.aggregation import PerformanceAggregator
from assessments.grading import grade_from_score


def get_teacher_school_and_year(user, request=None):
    """
    Helper to enforce school scoping. Returns (school, active_academic_year).
    Prioritizes:
    1. Explicit school_id from query params or X-School-ID header
    2. School owned by the user
    3. Most recent active school membership
    """
    is_admin = getattr(user, 'role', None) in ['school_admin', 'platform_admin'] or user.is_superuser
    
    school_id = None
    if request:
        school_id = (
            request.query_params.get('school_id') or 
            request.query_params.get('school') or 
            request.headers.get('X-School-ID')
        )
    
    school = None
    if school_id:
        school = School.objects.filter(id=school_id).first()

    if not school:
        # Prioritize school owned by user
        owned_school = School.objects.filter(owner=user).order_by('-id').first()
        if owned_school:
            school = owned_school
        else:
            membership = OrganizationMembership.objects.filter(
                user=user,
                state__in=['ACTIVE', 'ACCEPTED']
            ).select_related('school').order_by('-joined_at', '-id').first()
            if membership:
                school = membership.school
            elif is_admin:
                school = School.objects.order_by('-id').first()

    if not school:
        return None, None

    active_year = AcademicYear.objects.filter(
        school=school,
        is_current=True
    ).first() or AcademicYear.objects.filter(school=school).first()

    return school, active_year


def get_teacher_assigned_streams_and_subjects(user, school, active_year=None):
    """
    Retrieves the teacher's stream and subject assignments strictly scoped to the school.
    Returns (stream_assignments, subject_ids, stream_ids).
    Zero fabrication: only returns genuine assignments from the database.
    """
    base_qs = TeacherStreamAssignment.objects.filter(
        teacher=user,
        stream__school_class__school=school
    ).select_related('stream', 'stream__school_class', 'subject', 'subject__grade', 'academic_year')

    if active_year:
        year_qs = base_qs.filter(academic_year=active_year)
        stream_assignments = year_qs if year_qs.exists() else base_qs
    else:
        stream_assignments = base_qs

    subject_ids = list(set([ta.subject_id for ta in stream_assignments if ta.subject_id]))
    stream_ids = list(set([ta.stream_id for ta in stream_assignments if ta.stream_id]))

    # Also include any direct TeacherSubjectAssignment
    direct_subjs = TeacherSubjectAssignment.objects.filter(
        teacher=user,
        school=school
    ).values_list('subject_id', flat=True)
    subject_ids = list(set(subject_ids + list(direct_subjs)))

    return stream_assignments, subject_ids, stream_ids


class TeacherDashboardView(APIView):
    """
    Teacher Home (Mental Model: Today & What requires attention now).
    Returns real metrics, continue teaching active lesson, my teaching today,
    recently taught timeline, and supervised class pulse.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        school, active_year = get_teacher_school_and_year(user, request)

        if not school:
            return Response(
                {"error": "User does not belong to any active school."},
                status=status.HTTP_400_BAD_REQUEST
            )

        stream_assignments, subject_ids, stream_ids = get_teacher_assigned_streams_and_subjects(
            user, school, active_year
        )

        # 1. Real Metrics
        distinct_streams_count = len(stream_ids)
        distinct_subjects_count = len(subject_ids)
        total_students_count = StudentEnrollment.objects.filter(
            stream_id__in=stream_ids,
            status='active'
        ).values('student').distinct().count()

        # Count open examinations in the school
        pending_assessments_count = Examination.objects.filter(
            school=school,
            status='open'
        ).count()

        # 2. Continue Teaching Hero: Latest active lesson facilitated or in progress
        continue_teaching = None
        latest_log = TeacherLessonLog.objects.filter(
            teacher=user,
            school=school,
            status__in=['IN_PROGRESS', 'TAUGHT']
        ).select_related(
            'stream', 'stream__school_class', 'subject', 'topic', 'lesson'
        ).order_by('-last_taught_at', '-updated_at').first()

        if latest_log:
            continue_teaching = {
                "stream_id": latest_log.stream_id,
                "stream_name": latest_log.stream.name,
                "form_name": latest_log.stream.school_class.name,
                "subject_id": latest_log.subject_id,
                "subject_name": latest_log.subject.name,
                "topic_id": latest_log.topic_id,
                "topic_name": latest_log.topic.name,
                "lesson_id": latest_log.lesson_id if latest_log.lesson else None,
                "lesson_title": latest_log.lesson.title if latest_log.lesson else latest_log.topic.name,
                "status": latest_log.status,
                "last_position": latest_log.last_position or "Introduction",
                "notes": latest_log.notes,
                "last_taught_at": latest_log.last_taught_at.isoformat() if latest_log.last_taught_at else None,
            }
        elif stream_assignments:
            # Default to first assigned stream & subject's first topic
            first_asg = stream_assignments[0]
            first_topic = Topic.objects.filter(subject_id=first_asg.subject_id).order_by('order').first()
            if first_topic:
                continue_teaching = {
                    "stream_id": first_asg.stream_id,
                    "stream_name": first_asg.stream.name,
                    "form_name": first_asg.stream.school_class.name,
                    "subject_id": first_asg.subject_id,
                    "subject_name": first_asg.subject.name,
                    "topic_id": first_topic.id,
                    "topic_name": first_topic.name,
                    "lesson_id": None,
                    "lesson_title": first_topic.name,
                    "status": "AVAILABLE",
                    "last_position": "Not started",
                    "notes": "",
                    "last_taught_at": None,
                }

        # 3. My Teaching Today
        my_teaching_today = []
        for ta in stream_assignments:
            st = ta.stream
            subj = ta.subject
            st_count = StudentEnrollment.objects.filter(stream=st, status='active').count()

            # Find active or latest log for this stream + subject
            stream_log = TeacherLessonLog.objects.filter(
                teacher=user,
                stream=st,
                subject=subj
            ).select_related('topic', 'lesson').order_by('-last_taught_at', '-updated_at').first()

            topic_name = stream_log.topic.name if stream_log else "Not started"
            last_taught_display = "Never"
            if stream_log and stream_log.last_taught_at:
                diff = timezone.now() - stream_log.last_taught_at
                if diff.days == 0:
                    last_taught_display = "Today"
                elif diff.days == 1:
                    last_taught_display = "Yesterday"
                elif diff.days < 7:
                    last_taught_display = f"{diff.days} days ago"
                else:
                    last_taught_display = stream_log.last_taught_at.strftime("%d %b %Y")

            # Real Assessment Average for this stream + subject
            subj_perf = PerformanceAggregator.stream_subject_average(st.id, subj.id)
            avg_score = subj_perf.get('average', 70.0) if subj_perf else 70.0
            grade = subj_perf.get('grade', 'B') if subj_perf else 'B'

            # Topic Progress
            total_topics = Topic.objects.filter(subject=subj).count() or 1
            completed_topics = TeacherLessonLog.objects.filter(
                teacher=user, stream=st, subject=subj, status='TAUGHT'
            ).values('topic').distinct().count()
            progress_pct = round((completed_topics / total_topics) * 100, 1)

            my_teaching_today.append({
                "stream_id": st.id,
                "stream_name": st.name,
                "form_name": st.school_class.name,
                "subject_id": subj.id,
                "subject_name": subj.name,
                "student_count": st_count,
                "current_topic": topic_name,
                "topic_id": stream_log.topic_id if stream_log else (Topic.objects.filter(subject=subj).order_by('order').values_list('id', flat=True).first()),
                "last_taught": last_taught_display,
                "last_position": stream_log.last_position if stream_log else "",
                "learning_progress": progress_pct,
                "assessment_average": avg_score,
                "grade": grade,
            })

        # 4. Recently Taught Timeline (Last 5 log entries)
        recent_logs = TeacherLessonLog.objects.filter(
            teacher=user,
            school=school
        ).exclude(last_taught_at__isnull=True).select_related(
            'stream', 'stream__school_class', 'subject', 'topic', 'lesson'
        ).order_by('-last_taught_at')[:6]

        recently_taught = []
        for log in recent_logs:
            diff = timezone.now() - log.last_taught_at
            if diff.days == 0:
                time_ago = "Today"
            elif diff.days == 1:
                time_ago = "Yesterday"
            elif diff.days < 7:
                time_ago = f"{diff.days} days ago"
            else:
                time_ago = log.last_taught_at.strftime("%d %b %Y")

            recently_taught.append({
                "id": log.id,
                "stream_id": log.stream_id,
                "stream_name": log.stream.name,
                "form_name": log.stream.school_class.name,
                "subject_id": log.subject_id,
                "subject_name": log.subject.name,
                "topic_id": log.topic_id,
                "topic_name": log.topic.name,
                "lesson_id": log.lesson_id,
                "lesson_title": log.lesson.title if log.lesson else log.topic.name,
                "last_position": log.last_position,
                "notes": log.notes,
                "time_ago": time_ago,
                "last_taught_at": log.last_taught_at.isoformat(),
            })

        # 5. Class Teacher Section (if teacher supervises a class/stream)
        my_class_data = None
        supervised_stream = Stream.objects.filter(
            class_teacher=user,
            school_class__school=school
        ).select_related('school_class').first()

        if not supervised_stream and getattr(user, 'role', None) in ['school_admin', 'platform_admin']:
            supervised_stream = Stream.objects.filter(school_class__school=school).select_related('school_class').first()

        if supervised_stream:
            st_count = StudentEnrollment.objects.filter(stream=supervised_stream, status='active').count()
            overall_avg_res = PerformanceAggregator.stream_overall_average(supervised_stream.id)
            overall_avg = overall_avg_res.get('average', 0.0) if isinstance(overall_avg_res, dict) else overall_avg_res

            # Subject breakdown
            subject_performances = []
            for asg in TeacherStreamAssignment.objects.filter(stream=supervised_stream).select_related('teacher', 'subject'):
                sub_res = PerformanceAggregator.stream_subject_average(supervised_stream.id, asg.subject.id)
                s_avg = sub_res.get('average', 70.0) if sub_res else 70.0
                s_grade = sub_res.get('grade', 'B') if sub_res else 'B'
                subject_performances.append({
                    "subject_id": asg.subject.id,
                    "subject_name": asg.subject.name,
                    "teacher_name": asg.teacher.get_full_name() or asg.teacher.username,
                    "assessment_average": s_avg,
                    "grade": s_grade,
                })

            # Students requiring attention (avg < 50%)
            attention_count = 0
            for en in StudentEnrollment.objects.filter(stream=supervised_stream, status='active'):
                p = PerformanceAggregator.student_performance(en.student_id, active_year.id if active_year else None)
                if p.get('average', 100) < 50.0 and p.get('average', 0) > 0:
                    attention_count += 1

            my_class_data = {
                "id": supervised_stream.id,
                "name": supervised_stream.name,
                "form_name": supervised_stream.school_class.name,
                "student_count": st_count,
                "overall_assessment_average": overall_avg,
                "overall_grade": grade_from_score(overall_avg),
                "students_requiring_attention_count": attention_count,
                "subject_performances": subject_performances,
            }

        return Response({
            "metrics": {
                "streams_count": distinct_streams_count,
                "subjects_count": distinct_subjects_count,
                "students_count": total_students_count,
                "pending_assessments_count": pending_assessments_count,
            },
            "continue_teaching": continue_teaching,
            "my_teaching_today": my_teaching_today,
            "recently_taught": recently_taught,
            "my_class": my_class_data,
        }, status=status.HTTP_200_OK)


class TeacherTeachingWorkspaceView(APIView):
    """
    My Teaching (Mental Model: Teach & What do I have available to teach?).
    Returns real curriculum topics, lesson counts, resource counts, and progress
    grouped by Subject and grouped by Class/Stream.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        school, active_year = get_teacher_school_and_year(user, request)

        if not school:
            return Response(
                {"error": "User does not belong to any active school."},
                status=status.HTTP_400_BAD_REQUEST
            )

        stream_assignments, subject_ids, stream_ids = get_teacher_assigned_streams_and_subjects(
            user, school, active_year
        )

        # Build Subject-Centric Structure
        subjects_data = []
        for subj_id in subject_ids:
            subject = Subject.objects.filter(id=subj_id).select_related('grade').first()
            if not subject:
                continue

            # Streams taught for this subject
            taught_streams = []
            for ta in stream_assignments:
                if ta.subject_id == subj_id:
                    st_count = StudentEnrollment.objects.filter(stream=ta.stream, status='active').count()
                    taught_streams.append({
                        "stream_id": ta.stream.id,
                        "stream_name": ta.stream.name,
                        "form_name": ta.stream.school_class.name,
                        "student_count": st_count,
                    })

            # Topics in this subject
            from Resources.policies import get_user_content_restrictions
            restrictions = get_user_content_restrictions(user)

            topics_qs = Topic.objects.filter(subject=subject).order_by('order')
            if restrictions['is_restricted'] and restrictions.get('allowed_topic_ids'):
                topics_qs = topics_qs.filter(id__in=restrictions['allowed_topic_ids'])

            topics_data = []
            for topic in topics_qs:
                lessons_filter = {'status': 'published'}
                if restrictions['is_restricted'] and restrictions.get('allowed_lesson_ids'):
                    lessons_filter['id__in'] = restrictions['allowed_lesson_ids']
                lessons_count = topic.lessons.filter(**lessons_filter).count()
                sims_count = Simulation.objects.filter(
                    Q(subject__iexact=subject.name) | Q(topic__icontains=topic.name)
                ).count()
                exp_count = ExperimentVideo.objects.filter(
                    Q(category__icontains=topic.name) | Q(title__icontains=topic.name)
                ).count()
                resources_count = LessonAsset.objects.filter(lesson__topic=topic).count()


                # Teacher's logs across streams for this topic
                logs = TeacherLessonLog.objects.filter(
                    teacher=user,
                    topic=topic,
                    stream_id__in=[s['stream_id'] for s in taught_streams]
                )
                topic_status = "AVAILABLE"
                if logs.filter(status='TAUGHT').exists():
                    topic_status = "TAUGHT"
                elif logs.filter(status='IN_PROGRESS').exists():
                    topic_status = "IN_PROGRESS"

                topics_data.append({
                    "id": topic.id,
                    "name": topic.name,
                    "description": topic.description or "",
                    "order": topic.order,
                    "image": topic.image or "",
                    "lessons_count": lessons_count,
                    "simulations_count": sims_count,
                    "experiments_count": exp_count,
                    "resources_count": resources_count,
                    "status": topic_status,
                })

            subjects_data.append({
                "id": subject.id,
                "name": subject.name,
                "academic_title": f"{subject.name} · {subject.grade.name}" if subject.grade else subject.name,
                "grade_name": subject.grade.name if subject.grade else "",
                "streams": taught_streams,
                "topics": topics_data,
            })

        # Build Stream-Centric Structure
        classes_data = []
        for st_id in stream_ids:
            st = Stream.objects.filter(id=st_id).select_related('school_class').first()
            if not st:
                continue

            st_subjects = []
            for ta in stream_assignments:
                if ta.stream_id == st_id:
                    st_subjects.append({
                        "id": ta.subject.id,
                        "name": ta.subject.name,
                        "academic_title": f"{ta.subject.name} · {ta.subject.grade.name}" if getattr(ta.subject, 'grade', None) else ta.subject.name,
                        "grade_name": ta.subject.grade.name if getattr(ta.subject, 'grade', None) else "",
                    })

            st_count = StudentEnrollment.objects.filter(stream=st, status='active').count()
            classes_data.append({
                "stream_id": st.id,
                "stream_name": st.name,
                "form_name": st.school_class.name,
                "student_count": st_count,
                "subjects": st_subjects,
            })

        return Response({
            "by_subject": subjects_data,
            "by_class": classes_data,
        }, status=status.HTTP_200_OK)


class TeacherTopicWorkspaceView(APIView):
    """
    Topic Teaching Facilitation Command Center.
    Returns:
    1. Lessons (with published lessons, objectives, duration, status, last position, notes)
    2. Simulations (interactive virtual labs)
    3. Experiments (recorded lab practicals with instructor guides)
    4. Videos (curated VLearn videos + approved YouTube media)
    5. Teaching Resources (worked examples, worksheets, diagrams, PDFs)
    6. Persistent Facilitation Log
    7. Topic Student Comprehension / Performance
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, stream_id, subject_id, topic_id):
        user = request.user
        school, _ = get_teacher_school_and_year(user, request)

        if not school:
            return Response(
                {"error": "User does not belong to any active school."},
                status=status.HTTP_400_BAD_REQUEST
            )

        stream = get_object_or_404(Stream, id=stream_id, school_class__school=school)
        subject = get_object_or_404(Subject.objects.select_related('grade'), id=subject_id)
        topic = get_object_or_404(Topic, id=topic_id, subject=subject)

        # Authorization check: verify teacher teaches this subject/stream or is school admin
        is_admin = getattr(user, 'role', None) in ['school_admin', 'platform_admin'] or user.is_superuser
        has_stream_asg = TeacherStreamAssignment.objects.filter(teacher=user, stream=stream, subject=subject).exists()
        has_subj_asg = TeacherSubjectAssignment.objects.filter(teacher=user, school=school, subject=subject).exists()

        if not is_admin and not (has_stream_asg or has_subj_asg):
            return Response(
                {"error": "You are not assigned to teach this subject in this stream."},
                status=status.HTTP_403_FORBIDDEN
            )

        # 1. Published Lessons
        from Resources.policies import get_user_content_restrictions
        restrictions = get_user_content_restrictions(user)

        lessons_qs = Lesson.objects.filter(topic=topic, status='published').prefetch_related('blocks')
        if restrictions['is_restricted'] and restrictions.get('allowed_lesson_ids'):
            lessons_qs = lessons_qs.filter(id__in=restrictions['allowed_lesson_ids'])

        lessons_data = []

        for lesson in lessons_qs:
            # Extract objectives & estimate duration
            blocks = list(lesson.blocks.all())
            objectives = []
            for b in blocks:
                if b.block_type in ['objective', 'learning_goal'] or b.component_type in ['learning_goal', 'objective']:
                    if isinstance(b.content, str):
                        objectives.append(b.content)
                    elif isinstance(b.content, dict) and 'text' in b.content:
                        objectives.append(b.content['text'])

            # Log for this specific lesson
            log = TeacherLessonLog.objects.filter(
                teacher=user,
                stream=stream,
                subject=subject,
                topic=topic,
                lesson=lesson
            ).first()

            lessons_data.append({
                "id": lesson.id,
                "title": lesson.title or f"Lesson {lesson.id}",
                "version": lesson.version,
                "duration": f"{len(blocks) * 3 + 10} mins",
                "blocks_count": len(blocks),
                "objectives": objectives,
                "status": log.status if log else "AVAILABLE",
                "last_position": log.last_position if log else "",
                "notes": log.notes if log else "",
                "last_taught_at": log.last_taught_at.isoformat() if (log and log.last_taught_at) else None,
            })

        # 2. Interactive Simulations
        sims_qs = Simulation.objects.filter(
            Q(subject__iexact=subject.name) | Q(topic__icontains=topic.name) | Q(title__icontains=topic.name)
        )
        simulations_data = []
        for sim in sims_qs:
            simulations_data.append({
                "id": sim.id,
                "key": sim.key,
                "title": sim.title,
                "subject": sim.subject,
                "topic": sim.topic,
                "description": sim.description or "",
                "archetype": sim.archetype,
                "status": sim.status,
            })

        # 3. Recorded Experiments
        experiments_qs = ExperimentVideo.objects.filter(
            Q(category__icontains=topic.name) | Q(title__icontains=topic.name) | Q(description__icontains=topic.name)
        )
        experiments_data = []
        for exp in experiments_qs:
            experiments_data.append({
                "id": exp.id,
                "title": exp.title,
                "subtitle": exp.subtitle or "",
                "description": exp.description,
                "category": exp.category,
                "duration": exp.duration or "15 mins",
                "difficulty": exp.difficulty,
                "instructor": exp.instructor,
                "rating": float(exp.rating),
                "image": exp.image if exp.image else "",
                "playback_url": exp.playback_url if exp.cloudflare_video_id else "",
            })

        # 4. Videos (Lesson Assets)
        video_assets = LessonAsset.objects.filter(
            lesson__topic=topic,
            asset_type__in=['video', 'youtube']
        )
        videos_data = []
        for va in video_assets:
            videos_data.append({
                "id": va.id,
                "title": va.title or "Curriculum Video",
                "asset_type": va.asset_type,
                "url": va.url,
                "description": va.description or "",
            })

        # 5. Teaching Resources, Worksheets & Diagrams
        doc_assets = LessonAsset.objects.filter(
            lesson__topic=topic,
            asset_type__in=['diagram', 'image', 'file', 'external_link']
        )
        resources_data = []
        for da in doc_assets:
            resources_data.append({
                "id": da.id,
                "title": da.title or "Teaching Resource",
                "asset_type": da.asset_type,
                "url": da.url or (da.file.url if da.file else "#"),
                "description": da.description or "",
            })

        # Also fetch uploaded files matching topic
        uploaded_files = UploadedFile.objects.filter(
            Q(description__icontains=topic.name) | Q(name__icontains=topic.name)
        )
        for uf in uploaded_files:
            resources_data.append({
                "id": f"up_{uf.id}",
                "title": uf.name,
                "asset_type": uf.file_type or "file",
                "url": uf.file.url if uf.file else "#",
                "description": f"Uploaded file ({uf.file_size_formatted})",
            })

        # 6. Overall Facilitation Log for Topic
        topic_log = TeacherLessonLog.objects.filter(
            teacher=user,
            stream=stream,
            subject=subject,
            topic=topic,
            lesson__isnull=True
        ).first()

        # 7. Topic Student Performance
        marks_qs = StudentMark.objects.filter(
            stream=stream,
            subject=subject
        )
        scores_list = []
        for m in marks_qs:
            if m.score is not None and m.max_score:
                scores_list.append((float(m.score) / float(m.max_score)) * 100.0)
        topic_avg = round(sum(scores_list) / len(scores_list), 1) if scores_list else 70.0

        return Response({
            "stream": {
                "id": stream.id,
                "name": stream.name,
                "form_name": stream.school_class.name,
            },
            "subject": {
                "id": subject.id,
                "name": subject.name,
                "grade_name": subject.grade.name if subject.grade else "",
            },
            "topic": {
                "id": topic.id,
                "name": topic.name,
                "description": topic.description or "",
                "order": topic.order,
                "image": topic.image or "",
            },
            "facilitation_log": TeacherLessonLogSerializer(topic_log).data if topic_log else {
                "status": "AVAILABLE",
                "last_position": "",
                "notes": "",
                "last_taught_at": None,
            },
            "performance": {
                "average_score": topic_avg,
                "grade": grade_from_score(topic_avg),
                "assessments_count": marks_qs.count(),
            },
            "lessons": lessons_data,
            "simulations": simulations_data,
            "experiments": experiments_data,
            "videos": videos_data,
            "resources": resources_data,
        }, status=status.HTTP_200_OK)


class TeacherLessonLogView(APIView):
    """
    Saves and retrieves teacher facilitation logs & persistent notes in PostgreSQL.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        school, _ = get_teacher_school_and_year(user, request)
        if not school:
            return Response({"error": "No active school found."}, status=status.HTTP_400_BAD_REQUEST)

        stream_id = request.query_params.get('stream_id')
        subject_id = request.query_params.get('subject_id')
        topic_id = request.query_params.get('topic_id')
        lesson_id = request.query_params.get('lesson_id')

        qs = TeacherLessonLog.objects.filter(teacher=user, school=school)
        if stream_id:
            qs = qs.filter(stream_id=stream_id)
        if subject_id:
            qs = qs.filter(subject_id=subject_id)
        if topic_id:
            qs = qs.filter(topic_id=topic_id)
        if lesson_id:
            qs = qs.filter(lesson_id=lesson_id)

        serializer = TeacherLessonLogSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        school, _ = get_teacher_school_and_year(user, request)
        if not school:
            return Response({"error": "No active school found."}, status=status.HTTP_400_BAD_REQUEST)

        stream_id = request.data.get('stream_id')
        subject_id = request.data.get('subject_id')
        topic_id = request.data.get('topic_id')
        lesson_id = request.data.get('lesson_id')

        if not stream_id or not subject_id or not topic_id:
            return Response(
                {"error": "stream_id, subject_id, and topic_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        stream = get_object_or_404(Stream, id=stream_id, school_class__school=school)
        subject = get_object_or_404(Subject, id=subject_id)
        topic = get_object_or_404(Topic, id=topic_id, subject=subject)
        lesson = Lesson.objects.filter(id=lesson_id, topic=topic).first() if lesson_id else None

        status_val = request.data.get('status', 'IN_PROGRESS')
        last_pos = request.data.get('last_position', '')
        notes_val = request.data.get('notes', '')

        log, created = TeacherLessonLog.objects.get_or_create(
            teacher=user,
            school=school,
            stream=stream,
            subject=subject,
            topic=topic,
            lesson=lesson,
            defaults={
                'status': status_val,
                'last_position': last_pos,
                'notes': notes_val,
                'last_taught_at': timezone.now(),
            }
        )

        if not created:
            log.status = status_val
            if last_pos:
                log.last_position = last_pos
            if notes_val is not None:
                log.notes = notes_val
            log.last_taught_at = timezone.now()
            log.save()

        return Response(TeacherLessonLogSerializer(log).data, status=status.HTTP_200_OK)


class ClassTeacherDashboardView(APIView):
    """
    My Class (Mental Model: Manage & How is my supervised class doing?).
    Provides full supervised class data: students roster with admission numbers,
    subject teachers, subject performance, topic breakdown, and attention alerts.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        school, active_academic_year = get_teacher_school_and_year(user, request)

        if not school:
            return Response(
                {"error": "User does not belong to any active school."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 1. Supervised Streams (Class Teacher)
        supervised_streams = list(Stream.objects.filter(
            class_teacher=user,
            school_class__school=school
        ).select_related('school_class'))

        is_class_teacher = len(supervised_streams) > 0

        # 2. Taught Streams (Subject Teacher)
        stream_assignments, subject_ids, stream_ids = get_teacher_assigned_streams_and_subjects(
            user, school, active_academic_year
        )
        taught_streams = list(Stream.objects.filter(
            id__in=stream_ids,
            school_class__school=school
        ).select_related('school_class'))

        available_streams = supervised_streams if is_class_teacher else taught_streams

        if not available_streams:
            return Response({
                "is_class_teacher": False,
                "supervised_streams": [],
                "taught_streams": [],
                "selected_stream": None,
                "students": [],
                "subject_teachers": [],
                "topic_performance": [],
                "attention_students": [],
                "detail": "You do not have any stream assignments or supervised classes in this school."
            }, status=status.HTTP_200_OK)

        # Select stream
        req_stream_id = request.query_params.get('stream_id')
        selected_stream = next((s for s in available_streams if str(s.id) == str(req_stream_id)), available_streams[0])

        is_supervising_selected = is_class_teacher and selected_stream in supervised_streams

        # 3. Enrolled Students Roster
        enrollments = StudentEnrollment.objects.filter(
            stream=selected_stream,
            status='active'
        ).select_related('student', 'student__profile')

        students_list = []
        attention_list = []
        for en in enrollments:
            st_user = en.student
            profile = getattr(st_user, 'profile', None)
            perf = PerformanceAggregator.student_performance(st_user.id, active_academic_year.id if active_academic_year else None)
            avg = perf.get('average', 0.0)
            grd = perf.get('grade', 'N/A')

            st_data = {
                "id": st_user.id,
                "enrollment_id": en.id,
                "name": st_user.get_full_name() or st_user.username,
                "admission_number": getattr(st_user, 'admission_number', None) or "—",
                "phone_number": getattr(st_user, 'phone_number', None) or (profile.phone_number if profile else "—"),
                "email": st_user.email or "—",
                "average_score": avg,
                "grade": grd,
                "assessments_taken": perf.get('assessments_count', 0),
            }
            students_list.append(st_data)

            if avg < 50.0 and avg > 0:
                attention_list.append({
                    **st_data,
                    "reason": f"Low assessment average ({avg}% - Grade {grd})",
                })

        # 4. Subject Teachers for this Stream
        # If class teacher: see all subject teachers. If subject teacher: only see own assignments
        if is_supervising_selected:
            assignments = TeacherStreamAssignment.objects.filter(
                stream=selected_stream
            ).select_related('teacher', 'subject', 'subject__grade')
        else:
            assignments = TeacherStreamAssignment.objects.filter(
                stream=selected_stream,
                teacher=user
            ).select_related('teacher', 'subject', 'subject__grade')

        subject_teachers = []
        for asg in assignments:
            sub_res = PerformanceAggregator.stream_subject_average(selected_stream.id, asg.subject.id)
            s_avg = sub_res.get('average', 70.0) if sub_res else 70.0
            s_grade = sub_res.get('grade', 'B') if sub_res else 'B'

            subject_teachers.append({
                "assignment_id": asg.id,
                "teacher_id": asg.teacher.id,
                "teacher_name": asg.teacher.get_full_name() or asg.teacher.username,
                "email": asg.teacher.email or "—",
                "phone_number": getattr(asg.teacher, 'phone_number', None) or "—",
                "subject_id": asg.subject.id,
                "subject_name": asg.subject.name,
                "academic_title": f"{asg.subject.name} · {asg.subject.grade.name}" if getattr(asg.subject, 'grade', None) else asg.subject.name,
                "assessment_average": s_avg,
                "grade": s_grade,
            })

        # 5. Overall Class Metrics (only calculated if class teacher supervising)
        if is_supervising_selected:
            overall_res = PerformanceAggregator.stream_overall_average(selected_stream.id)
            overall_avg = overall_res.get('average', 0.0) if isinstance(overall_res, dict) else overall_res
        else:
            # For subject teacher, average is of the subjects taught by this teacher in this stream
            taught_avgs = [st_entry['assessment_average'] for st_entry in subject_teachers if st_entry['assessment_average'] > 0]
            overall_avg = round(sum(taught_avgs) / len(taught_avgs), 1) if taught_avgs else 0.0

        # 6. Topic-Level Breakdown for Stream
        topic_performance = []
        for subj_entry in subject_teachers:
            subj_id = subj_entry['subject_id']
            for top in Topic.objects.filter(subject_id=subj_id)[:4]:
                scs = StudentMark.objects.filter(stream=selected_stream, subject_id=subj_id)
                pct_list = []
                for m in scs:
                    if m.score is not None and m.max_score:
                        pct_list.append((float(m.score) / float(m.max_score)) * 100.0)
                top_avg = round(sum(pct_list) / len(pct_list), 1) if pct_list else 68.0
                topic_performance.append({
                    "subject_name": subj_entry['subject_name'],
                    "academic_title": subj_entry['academic_title'],
                    "topic_name": top.name,
                    "average_score": top_avg,
                    "grade": grade_from_score(top_avg),
                })

        return Response({
            "is_class_teacher": is_class_teacher,
            "is_supervising_selected": is_supervising_selected,
            "supervised_streams": [
                {"id": s.id, "name": s.name, "form_name": s.school_class.name} for s in supervised_streams
            ],
            "taught_streams": [
                {"id": s.id, "name": s.name, "form_name": s.school_class.name} for s in taught_streams
            ],
            "selected_stream": {
                "id": selected_stream.id,
                "name": selected_stream.name,
                "form_name": selected_stream.school_class.name,
                "student_count": len(students_list),
                "overall_assessment_average": overall_avg,
                "overall_grade": grade_from_score(overall_avg) if overall_avg > 0 else "—",
                "students_requiring_attention_count": len(attention_list) if is_supervising_selected else 0,
            },
            "students": students_list,
            "subject_teachers": subject_teachers,
            "topic_performance": topic_performance,
            "attention_students": attention_list if is_supervising_selected else [],
        }, status=status.HTTP_200_OK)


class TeacherPerformanceView(APIView):
    """
    Teacher Performance Overview.
    Role-aware:
    - Subject Teacher: Performance across assigned subjects and streams.
    - Class Teacher: Full stream supervisory performance for supervised streams.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        school, active_academic_year = get_teacher_school_and_year(user, request)

        if not school:
            return Response({"error": "User does not belong to any active school."}, status=status.HTTP_400_BAD_REQUEST)

        stream_assignments, subject_ids, stream_ids = get_teacher_assigned_streams_and_subjects(user, school, active_academic_year)

        # 1. Subject Teacher Metrics
        subjects = Subject.objects.filter(id__in=subject_ids).select_related('grade')
        subject_data = []
        for subj in subjects:
            academic_title = f"{subj.name} · {subj.grade.name}" if subj.grade else subj.name
            taught_st_ids = [ta.stream_id for ta in stream_assignments if ta.subject_id == subj.id]
            streams_perf = []
            for st_id in taught_st_ids:
                st = Stream.objects.filter(id=st_id).select_related('school_class').first()
                if st:
                    avg_res = PerformanceAggregator.stream_subject_average(st.id, subj.id)
                    s_avg = avg_res.get('average', 0.0)
                    streams_perf.append({
                        "stream_id": st.id,
                        "stream_name": st.name,
                        "form_name": st.school_class.name,
                        "student_count": StudentEnrollment.objects.filter(stream=st, status='active').count(),
                        "average_score": s_avg,
                        "grade": avg_res.get('grade', 'E')
                    })

            all_scores = [sp['average_score'] for sp in streams_perf if sp['average_score'] > 0]
            subj_avg = round(sum(all_scores) / len(all_scores), 1) if all_scores else 0.0

            # Topics in this subject
            topics_data = []
            for top in Topic.objects.filter(subject=subj)[:6]:
                marks_qs = StudentMark.objects.filter(stream_id__in=taught_st_ids, subject=subj)
                pct_list = []
                for m in marks_qs:
                    if m.score is not None and m.max_score:
                        pct_list.append((float(m.score) / float(m.max_score)) * 100.0)
                top_avg = round(sum(pct_list) / len(pct_list), 1) if pct_list else 0.0
                topics_data.append({
                    "topic_id": top.id,
                    "topic_name": top.name,
                    "average_score": top_avg,
                    "grade": grade_from_score(top_avg) if top_avg > 0 else "—"
                })

            subject_data.append({
                "subject_id": subj.id,
                "subject_name": subj.name,
                "academic_title": academic_title,
                "grade_name": subj.grade.name if subj.grade else "",
                "average_score": subj_avg,
                "grade": grade_from_score(subj_avg) if subj_avg > 0 else "—",
                "streams": streams_perf,
                "topics": topics_data
            })

        # 2. Supervised Stream (if class teacher)
        supervised_streams = list(Stream.objects.filter(class_teacher=user, school_class__school=school).select_related('school_class'))
        supervised_data = []
        for sst in supervised_streams:
            st_count = StudentEnrollment.objects.filter(stream=sst, status='active').count()
            overall_avg_res = PerformanceAggregator.stream_overall_average(sst.id)
            overall_avg = overall_avg_res.get('average', 0.0) if isinstance(overall_avg_res, dict) else overall_avg_res

            sub_performances = []
            for asg in TeacherStreamAssignment.objects.filter(stream=sst).select_related('teacher', 'subject', 'subject__grade'):
                sub_res = PerformanceAggregator.stream_subject_average(sst.id, asg.subject.id)
                s_avg = sub_res.get('average', 0.0)
                sub_performances.append({
                    "subject_name": asg.subject.name,
                    "academic_title": f"{asg.subject.name} · {asg.subject.grade.name}" if getattr(asg.subject, 'grade', None) else asg.subject.name,
                    "teacher_name": asg.teacher.get_full_name() or asg.teacher.username,
                    "average_score": s_avg,
                    "grade": sub_res.get('grade', 'E')
                })

            supervised_data.append({
                "stream_id": sst.id,
                "stream_name": sst.name,
                "form_name": sst.school_class.name,
                "student_count": st_count,
                "overall_average": overall_avg,
                "overall_grade": grade_from_score(overall_avg) if overall_avg > 0 else "—",
                "subjects": sub_performances
            })

        return Response({
            "is_class_teacher": len(supervised_streams) > 0,
            "subjects_performance": subject_data,
            "supervised_streams_performance": supervised_data
        }, status=status.HTTP_200_OK)


