from django.db.models import Avg
from .models import StudentMark
from .grading import grade_from_score

class PerformanceAggregator:
    @staticmethod
    def student_performance(student_id, academic_year_id=None, term=None, examination_id=None):
        qs = StudentMark.objects.filter(student_id=student_id)
        if academic_year_id:
            qs = qs.filter(academic_year_id=academic_year_id)
        if term:
            qs = qs.filter(examination__term=term)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)

        subjects = []
        for mark in qs.select_related('subject', 'examination'):
            score = float(mark.score) if mark.score is not None else 0.0
            max_s = mark.max_score or 100
            subjects.append({
                'subject_id': mark.subject_id,
                'subject_name': mark.subject.name if mark.subject else 'Subject',
                'exam_name': mark.examination.name if mark.examination else '',
                'score': score,
                'max_score': max_s,
                'grade': grade_from_score(score, max_s)
            })

        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float),
            'subjects': subjects
        }

    @staticmethod
    def student_subject_history(student_id, subject_id, academic_year_id=None):
        qs = StudentMark.objects.filter(student_id=student_id, subject_id=subject_id)
        if academic_year_id:
            qs = qs.filter(academic_year_id=academic_year_id)
        return list(qs.values('examination__name', 'score', 'examination__term', 'entered_at').order_by('examination__sequence'))

    @staticmethod
    def stream_subject_average(stream_id, subject_id, examination_id=None):
        qs = StudentMark.objects.filter(stream_id=stream_id, subject_id=subject_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def stream_overall_average(stream_id, examination_id=None):
        qs = StudentMark.objects.filter(stream_id=stream_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)

        subject_averages = []
        from django.db.models import Count
        sub_qs = qs.values('subject_id', 'subject__name').annotate(
            avg_score=Avg('score'), count=Count('id')
        )
        for s in sub_qs:
            sub_avg = round(float(s['avg_score'] or 0), 1)
            subject_averages.append({
                'subject_id': s['subject_id'],
                'subject_name': s['subject__name'],
                'average': sub_avg,
                'grade': grade_from_score(sub_avg),
                'candidate_count': s['count']
            })

        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float),
            'subject_averages': subject_averages
        }

    @staticmethod
    def form_subject_average(school_class_id, subject_id, examination_id=None):
        qs = StudentMark.objects.filter(stream__school_class_id=school_class_id, subject_id=subject_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def form_overall_average(school_class_id, examination_id=None):
        qs = StudentMark.objects.filter(stream__school_class_id=school_class_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)

        stream_breakdown = []
        from organizations.models import Stream, StudentEnrollment
        streams = Stream.objects.filter(school_class_id=school_class_id).select_related('class_teacher')
        for stream in streams:
            stream_marks = qs.filter(stream=stream)
            stream_avg = stream_marks.aggregate(s_avg=Avg('score'))['s_avg'] or 0.0
            stream_avg_float = round(float(stream_avg), 1)
            student_count = StudentEnrollment.objects.filter(stream=stream, status='active').count()
            stream_breakdown.append({
                'stream_id': stream.id,
                'stream_name': stream.name,
                'class_teacher': f"{stream.class_teacher.first_name} {stream.class_teacher.last_name}".strip() if stream.class_teacher else None,
                'student_count': student_count,
                'average': stream_avg_float,
                'grade': grade_from_score(stream_avg_float)
            })

        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float),
            'streams': stream_breakdown
        }

    @staticmethod
    def school_subject_average(school_id, subject_id, examination_id=None):
        qs = StudentMark.objects.filter(examination__school_id=school_id, subject_id=subject_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def school_overall_average(school_id, examination_id=None):
        qs = StudentMark.objects.filter(examination__school_id=school_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def student_longitudinal_record(student_id):
        return list(StudentMark.objects.filter(student_id=student_id).values(
            'academic_year__name', 'examination__name', 'subject__name', 'score'
        ).order_by('academic_year__start_date', 'examination__sequence'))
