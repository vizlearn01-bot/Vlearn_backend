import hashlib
import secrets
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Q

from organizations.models import (
    School,
    OrganizationMembership,
    TeacherSubjectAssignment,
    TeacherStreamAssignment,
    StudentEnrollment,
    SchoolSubscription,
    SchoolInvitation,
    TeacherSpecialty,
    Term,
    ExamConfiguration,
)


class EntitlementService:
    @staticmethod
    def has_full_curriculum_access(user) -> bool:
        if not user or not user.is_authenticated:
            return False

        from Resources.policies import get_user_content_restrictions
        restrictions = get_user_content_restrictions(user)
        if restrictions['is_restricted']:
            return False

        return True

    @staticmethod
    def get_allowed_subject_ids(user) -> list:
        from curriculum.models import Subject
        if not user or not user.is_authenticated:
            return []

        from Resources.policies import get_user_content_restrictions
        restrictions = get_user_content_restrictions(user)
        if restrictions['is_restricted']:
            return restrictions['allowed_subject_ids']

        return list(Subject.objects.values_list('id', flat=True))

    @staticmethod
    def check_curriculum_access(user, subject_id) -> bool:
        """
        Determines if a user has access to curriculum/lessons for a given subject.
        """
        if not user or not user.is_authenticated:
            return False

        from Resources.policies import get_user_content_restrictions
        restrictions = get_user_content_restrictions(user)
        if restrictions['is_restricted']:
            return int(subject_id) in restrictions['allowed_subject_ids']

        return True


    @staticmethod
    def enforce_teacher_capacity(school) -> None:
        """
        Raises ValidationError if (active teachers + pending teacher invitations) >= subscription.max_teachers.
        Uses row lock on SchoolSubscription to prevent race conditions under concurrent requests.
        """
        from django.db import transaction
        with transaction.atomic():
            now = timezone.now()
            subscription = SchoolSubscription.objects.select_for_update().filter(
                school=school, is_active=True, end_date__gte=now
            ).order_by('-id').first()
            if not subscription:
                # Auto-provision active standard trial subscription for the school
                subscription = SchoolSubscription.objects.create(
                    school=school,
                    max_teachers=50,
                    max_students=2000,
                    is_active=True,
                    start_date=now,
                    end_date=now + timedelta(days=365)
                )

            active_count = OrganizationMembership.objects.filter(
                school=school,
                role='teacher',
                state__in=['ACCEPTED', 'ACTIVE']
            ).count()

            pending_invites = SchoolInvitation.objects.filter(
                school=school,
                role='teacher',
                state='PENDING',
                expires_at__gt=now
            ).count()

            if (active_count + pending_invites) >= subscription.max_teachers:
                raise ValidationError(f"Teacher capacity limit reached ({subscription.max_teachers} max seats).")

    @staticmethod
    def enforce_student_capacity(school) -> None:
        """
        Raises ValidationError if active enrolled students >= subscription.max_students.
        Uses row lock on SchoolSubscription to prevent race conditions under concurrent requests.
        """
        from django.db import transaction
        with transaction.atomic():
            now = timezone.now()
            subscription = SchoolSubscription.objects.select_for_update().filter(
                school=school, is_active=True, end_date__gte=now
            ).order_by('-id').first()
            if not subscription:
                # Auto-provision active standard trial subscription for the school
                subscription = SchoolSubscription.objects.create(
                    school=school,
                    max_teachers=50,
                    max_students=2000,
                    is_active=True,
                    start_date=now,
                    end_date=now + timedelta(days=365)
                )

            enrolled_count = StudentEnrollment.objects.filter(
                stream__school_class__school=school,
                status='active'
            ).count()

            pending_invites = SchoolInvitation.objects.filter(
                school=school,
                role='student',
                state='PENDING',
                expires_at__gt=now
            ).count()

            if (enrolled_count + pending_invites) >= subscription.max_students:
                raise ValidationError(f"Student capacity limit reached ({subscription.max_students} max seats).")

    @staticmethod
    def transition_membership_state(membership, new_state, actor=None) -> OrganizationMembership:
        """
        Transitions membership state (PENDING -> ACCEPTED -> ACTIVE -> SUSPENDED -> ARCHIVED)
        with validation.
        """
        valid_transitions = {
            'PENDING': ['ACCEPTED', 'SUSPENDED', 'ARCHIVED'],
            'ACCEPTED': ['ACTIVE', 'SUSPENDED', 'ARCHIVED'],
            'ACTIVE': ['SUSPENDED', 'ARCHIVED'],
            'SUSPENDED': ['ACTIVE', 'ACCEPTED', 'ARCHIVED'],
            'ARCHIVED': ['PENDING', 'ACCEPTED', 'ACTIVE'],
        }

        if membership.state == new_state:
            return membership

        allowed = valid_transitions.get(membership.state, [])
        if new_state not in allowed:
            raise ValidationError(
                f"Invalid membership state transition from {membership.state} to {new_state}."
            )

        if membership.state not in ['ACCEPTED', 'ACTIVE'] and new_state in ['ACCEPTED', 'ACTIVE']:
            if membership.role == 'teacher':
                EntitlementService.enforce_teacher_capacity(membership.school)
            elif membership.role == 'student':
                EntitlementService.enforce_student_capacity(membership.school)

        membership.state = new_state
        if actor and hasattr(actor, 'pk'):
            membership.assigned_by = actor
        membership.save()
        return membership

    @staticmethod
    def create_school_invitation(
        school,
        role,
        created_by,
        phone_number=None,
        email='',
        intended_class=None,
        intended_stream=None,
        intended_subject=None
    ) -> SchoolInvitation:
        """
        Enforces teacher/student seat capacity before creating invitation.
        """
        if role == 'teacher':
            EntitlementService.enforce_teacher_capacity(school)
        elif role == 'student':
            EntitlementService.enforce_student_capacity(school)

        raw_token = secrets.token_urlsafe(32)
        token_hash = hashlib.sha256(raw_token.encode('utf-8')).hexdigest()
        expires_at = timezone.now() + timedelta(days=7)

        invitation = SchoolInvitation.objects.create(
            school=school,
            email=email or '',
            phone_number=phone_number,
            role=role,
            created_by=created_by,
            intended_class=intended_class,
            intended_stream=intended_stream,
            intended_subject=intended_subject,
            token_hash=token_hash,
            expires_at=expires_at,
            state='PENDING',
            invitation_type=f"{role}_invite"
        )
        invitation.raw_token = raw_token
        return invitation


class SchoolOnboardingService:
    @staticmethod
    def register_school_profile(user, payload):
        from .models import School, OrganizationMembership, AcademicYear, SchoolClass, Stream
        from curriculum.models import Grade
        from django.db import transaction
        from datetime import date
        from rest_framework.exceptions import ValidationError

        name = payload.get('name')
        code = payload.get('code')
        if not code:
            code = None
            
        if not name:
            raise ValidationError("School name is required.")

        if code and School.objects.filter(code=code).exists():
            raise ValidationError(f"School code '{code}' is already registered.")

        first_stream_data = payload.get('first_stream')

        with transaction.atomic():
            school = School.objects.create(
                name=name,
                code=code,
                owner=user,
                contact_email=payload.get('contact_email', user.email),
                phone_number=payload.get('phone_number', ''),
                address=payload.get('address', ''),
                school_type=payload.get('school_type', 'PUBLIC'),
                ownership_type=payload.get('ownership_type', 'PUBLIC'),
                curricula_offered=payload.get('curricula_offered', 'BOTH'),
                estimated_students=payload.get('number_of_students', 0),
                estimated_teachers=payload.get('estimated_teachers', 0),
                internet_access=payload.get('internet_access', 'LIMITED'),
                electricity_reliability=payload.get('electricity_reliability', 'RELIABLE'),
                available_devices=payload.get('available_devices', []),
                location_county=payload.get('location_county', ''),
                location_subcounty=payload.get('location_subcounty', ''),
                location_ward=payload.get('location_ward', ''),
                onboarding_version=1,
                setup_status='PROFILE_COMPLETE',
                completed_by=user
            )

            OrganizationMembership.objects.create(
                user=user,
                school=school,
                role='school_admin',
                state='ACTIVE',
                assigned_by=user
            )

            if first_stream_data:
                # 1. Create a sensible default Academic Year
                current_year = date.today().year
                academic_year = AcademicYear.objects.create(
                    school=school,
                    name=f"{current_year} Academic Year",
                    start_date=date(current_year, 1, 1),
                    end_date=date(current_year, 12, 31),
                    is_current=True
                )

                # 2. Get the Grade and create SchoolClass
                grade_id = first_stream_data.get('grade_id')
                if not grade_id:
                    raise ValidationError("Grade ID is required to create the first stream.")
                
                grade = Grade.objects.filter(id=grade_id).first()
                if not grade:
                    raise ValidationError("Invalid Grade ID provided.")
                
                school_class = SchoolClass.objects.create(
                    school=school,
                    curriculum_grade=grade,
                    name=grade.name, # Default to the grade name
                )

                # 3. Create Stream
                stream_name = first_stream_data.get('name')
                if not stream_name:
                    raise ValidationError("Stream name is required.")
                
                Stream.objects.create(
                    school_class=school_class,
                    name=stream_name
                )
                
                school.setup_status = 'STREAMS_CREATED'
                school.save(update_fields=['setup_status'])

        return school

    @staticmethod
    def get_school_setup_state(school):
        from .models import Stream, SchoolInvitation, TeacherSubjectAssignment, StudentEnrollment, AcademicExamination

        streams_count = Stream.objects.filter(school_class__school=school).count()
        invitations_count = SchoolInvitation.objects.filter(school=school).count()
        assignments_count = TeacherSubjectAssignment.objects.filter(school=school).count()
        students_count = StudentEnrollment.objects.filter(stream__school_class__school=school).count()
        exams_count = AcademicExamination.objects.filter(school=school).count()

        checklist = [
            {"key": "PROFILE_COMPLETE", "label": "Register School Profile", "complete": True},
            {"key": "STREAMS_CREATED", "label": "Create Academic Streams", "complete": streams_count > 0, "count": streams_count},
            {"key": "TEACHERS_INVITED", "label": "Invite Teachers", "complete": invitations_count > 0, "count": invitations_count},
            {"key": "SUBJECTS_ASSIGNED", "label": "Assign Teachers to Subjects", "complete": assignments_count > 0, "count": assignments_count},
            {"key": "STUDENTS_IMPORTED", "label": "Import / Enroll Students", "complete": students_count > 0, "count": students_count},
            {"key": "BASELINE_UPLOADED", "label": "Upload Historical Exam Baseline", "complete": exams_count > 0, "count": exams_count},
        ]

        # Calculate current status automatically based on progress
        current_status = school.setup_status
        if exams_count > 0 and students_count > 0 and assignments_count > 0:
            current_status = 'FULLY_CONFIGURED'

        return {
            "school_id": school.id,
            "school_name": school.name,
            "code": school.code,
            "onboarding_version": school.onboarding_version,
            "setup_status": current_status,
            "setup_draft_data": school.setup_draft_data,
            "completed_at": school.completed_at,
            "checklist": checklist
        }

    @staticmethod
    def save_setup_draft(school, draft_data, actor):
        school.setup_draft_data = draft_data
        school.save(update_fields=['setup_draft_data', 'updated_at'])
        # Commit entities into relational database tables so they appear on dashboard
        SchoolOnboardingService.commit_setup_data(school, draft_data, actor)
        return school

    @staticmethod
    def commit_setup_data(school, draft_data, actor):
        from .models import (
            AcademicYear, SchoolClass, Stream, Term, ExamConfiguration,
            TeacherSpecialty, TeacherStreamAssignment, StudentEnrollment
        )
        from Resources.models import User, UserProfile
        from curriculum.models import Curriculum, Grade, Subject
        from django.db import transaction
        import re

        if not draft_data or not isinstance(draft_data, dict):
            return school

        with transaction.atomic():
            school_profile = draft_data.get('schoolProfile', {})
            forms_streams = draft_data.get('formsStreams', {})
            teachers_list = draft_data.get('teachers', [])
            students_dict = draft_data.get('students', {})
            teacher_assignments = draft_data.get('teacherAssignments', {})
            exam_config = draft_data.get('examConfig', {})

            # 1. Academic Year
            acad_year_val = school_profile.get('academicYear') or '2026'
            acad_year_name = f"{acad_year_val} Academic Year"
            academic_year = AcademicYear.objects.filter(school=school, is_current=True).first()
            if not academic_year:
                academic_year = AcademicYear.objects.filter(school=school).first()
            if not academic_year:
                academic_year = AcademicYear.objects.create(
                    school=school,
                    name=acad_year_name,
                    start_date=f"{acad_year_val}-01-05",
                    end_date=f"{acad_year_val}-11-30",
                    is_current=True
                )
            if not academic_year.is_current:
                AcademicYear.objects.filter(school=school).update(is_current=False)
                academic_year.is_current = True
                academic_year.save(update_fields=['is_current'])

            # 2. Terms
            term_names = ['Term 1', 'Term 2', 'Term 3']
            curr_term = school_profile.get('currentTerm', 'Term 1')
            for i, t_name in enumerate(term_names):
                Term.objects.get_or_create(
                    school=school,
                    academic_year=academic_year,
                    number=i + 1,
                    defaults={
                        'name': t_name,
                        'is_current': (t_name == curr_term),
                        'start_date': f"{acad_year_val}-0{i*3+1}-05" if i < 3 else f"{acad_year_val}-09-05",
                        'end_date': f"{acad_year_val}-0{i*3+3}-30" if i < 3 else f"{acad_year_val}-11-30"
                    }
                )

            # 3. Exam Configurations
            if exam_config and exam_config.get('names'):
                names = [n.strip() for n in exam_config['names'] if n and str(n).strip()]
                if names:
                    exam_defs = [{"name": n, "sequence": idx + 1} for idx, n in enumerate(names)]
                    for term_num in [1, 2, 3]:
                        ExamConfiguration.objects.get_or_create(
                            school=school,
                            academic_year=academic_year,
                            term=term_num,
                            defaults={
                                'exam_count': len(names),
                                'exam_definitions': exam_defs
                            }
                        )

            # 4. Curriculum & Grade Resolution
            curriculum_val = school.curricula_offered or school_profile.get('curriculum', '')
            if 'CBC' in str(curriculum_val).upper():
                curriculum_obj = Curriculum.objects.filter(name__icontains='CBC').first() or Curriculum.objects.first()
            else:
                curriculum_obj = Curriculum.objects.filter(name__icontains='844').first() or Curriculum.objects.first()

            # 5. Forms and Streams
            form_stream_map = forms_streams.get('streams', {}) if isinstance(forms_streams, dict) else {}
            forms_list = forms_streams.get('forms', []) if isinstance(forms_streams, dict) else []
            if not forms_list and isinstance(form_stream_map, dict):
                forms_list = list(form_stream_map.keys())

            created_classes = {}
            created_streams = {}

            for form_name in forms_list:
                if not form_name or not str(form_name).strip():
                    continue
                form_clean = str(form_name).strip()

                digits = re.findall(r'\d+', form_clean)
                level_num = int(digits[0]) if digits else 1

                grade_obj = Grade.objects.filter(name__iexact=form_clean).first()
                if not grade_obj:
                    grade_obj, _ = Grade.objects.get_or_create(
                        curriculum=curriculum_obj,
                        name=form_clean,
                        defaults={'level': level_num}
                    )

                code = form_clean.upper().replace(' ', '')
                school_class = SchoolClass.objects.filter(school=school, name__iexact=form_clean).first()
                if not school_class:
                    school_class = SchoolClass.objects.create(
                        school=school,
                        name=form_clean,
                        curriculum_grade=grade_obj,
                        code=code
                    )
                elif school_class.curriculum_grade != grade_obj:
                    school_class.curriculum_grade = grade_obj
                    school_class.save(update_fields=['curriculum_grade'])

                created_classes[form_clean.lower()] = school_class

                # Streams
                streams_for_form = form_stream_map.get(form_name, []) or []
                for stream_name in streams_for_form:
                    if not stream_name or not str(stream_name).strip():
                        continue
                    st_clean = str(stream_name).strip()
                    stream_obj = Stream.objects.filter(school_class=school_class, name__iexact=st_clean).first()
                    if not stream_obj:
                        stream_obj = Stream.objects.create(
                            school_class=school_class,
                            name=st_clean
                        )
                    created_streams[f"{form_clean.lower()}-{st_clean.lower()}"] = stream_obj
                    created_streams[f"{form_clean}-{st_clean}"] = stream_obj

            # 6. Teachers
            created_teachers = {}
            for t in teachers_list:
                if not isinstance(t, dict):
                    continue
                t_name = t.get('name') or t.get('teacher_name') or ''
                t_phone = t.get('phone') or t.get('phone_number') or ''
                t_email = t.get('email') or None
                t_tsc = t.get('tsc_number') or t.get('tsc') or None
                t_specs = t.get('specialties') or ''

                if not t_name and not t_phone:
                    continue

                clean_phone = str(t_phone).strip().replace(' ', '').replace('-', '')
                if clean_phone.startswith('0'):
                    clean_phone = '+254' + clean_phone[1:]
                elif clean_phone.startswith('254'):
                    clean_phone = '+' + clean_phone

                t_user = None
                if clean_phone:
                    t_user = User.objects.filter(phone_number=clean_phone).first()
                if not t_user and t_email:
                    t_user = User.objects.filter(email__iexact=t_email).first()

                if not t_user:
                    names = str(t_name).strip().split(' ', 1)
                    first_name = names[0]
                    last_name = names[1] if len(names) > 1 else ''
                    username = f"teacher_{clean_phone.replace('+', '')}" if clean_phone else f"teacher_{school.code}_{secrets.token_hex(3)}"
                    t_user = User.objects.create(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        phone_number=clean_phone or '',
                        email=t_email,
                        role='teacher',
                        tsc_number=t_tsc,
                    )
                    t_user.set_unusable_password()
                    t_user.save()
                    UserProfile.objects.get_or_create(user=t_user)
                else:
                    if t_name:
                        names = str(t_name).strip().split(' ', 1)
                        t_user.first_name = names[0]
                        if len(names) > 1:
                            t_user.last_name = names[1]
                    if t_tsc and not t_user.tsc_number:
                        t_user.tsc_number = t_tsc
                    if t_email and not t_user.email:
                        t_user.email = t_email
                    t_user.save()

                if not OrganizationMembership.objects.filter(user=t_user, school=school).exists():
                    OrganizationMembership.objects.create(
                        user=t_user,
                        school=school,
                        role='teacher',
                        state='ACTIVE',
                        assigned_by=actor if getattr(actor, 'is_authenticated', False) else None
                    )

                if t_specs:
                    specs = [s.strip() for s in str(t_specs).split(',') if s.strip()]
                    for spec_name in specs:
                        sub = Subject.objects.filter(name__iexact=spec_name).first()
                        if sub and not TeacherSpecialty.objects.filter(teacher=t_user, subject=sub, school=school).exists():
                            TeacherSpecialty.objects.create(
                                teacher=t_user,
                                subject=sub,
                                school=school
                            )

                if clean_phone:
                    created_teachers[clean_phone] = t_user
                if t.get('id'):
                    created_teachers[str(t.get('id'))] = t_user
                created_teachers[str(t_name).lower()] = t_user

            # 7. Students
            for stream_key, st_list in students_dict.items():
                if not isinstance(st_list, list):
                    continue
                stream_obj = created_streams.get(str(stream_key).lower()) or created_streams.get(str(stream_key))
                if not stream_obj:
                    parts = str(stream_key).split('-', 1)
                    if len(parts) == 2:
                        stream_obj = Stream.objects.filter(
                            school_class__school=school,
                            school_class__name__iexact=parts[0].strip(),
                            name__iexact=parts[1].strip()
                        ).first()

                if not stream_obj:
                    continue

                for st in st_list:
                    if not isinstance(st, dict):
                        continue
                    st_name = st.get('name') or ''
                    st_adm = st.get('admNo') or st.get('admission_number') or ''
                    if not st_name and not st_adm:
                        continue

                    clean_adm = str(st_adm).strip()
                    names = str(st_name).strip().split(' ', 1)
                    first_name = names[0]
                    last_name = names[1] if len(names) > 1 else ''

                    st_username = f"student_{school.code}_{clean_adm.replace(' ', '')}" if clean_adm else f"student_{school.id}_{secrets.token_hex(4)}"

                    st_user = User.objects.filter(username=st_username).first()
                    if not st_user:
                        st_user = User.objects.create(
                            username=st_username,
                            first_name=first_name,
                            last_name=last_name,
                            role='student',
                        )
                        st_user.set_unusable_password()
                        st_user.save()
                    else:
                        st_user.first_name = first_name
                        st_user.last_name = last_name
                        st_user.save()

                    profile, _ = UserProfile.objects.get_or_create(user=st_user)
                    profile.verified_school = school
                    profile.school = school.name
                    profile.school_association_type = 'VERIFIED_ORGANIZATION'
                    if stream_obj.school_class and stream_obj.school_class.curriculum_grade:
                        profile.curriculum_grade = stream_obj.school_class.curriculum_grade
                        profile.grade = stream_obj.school_class.name
                    profile.save()

                    if not OrganizationMembership.objects.filter(user=st_user, school=school).exists():
                        OrganizationMembership.objects.create(
                            user=st_user,
                            school=school,
                            role='student',
                            state='ACTIVE',
                            assigned_by=actor if getattr(actor, 'is_authenticated', False) else None
                        )

                    if not StudentEnrollment.objects.filter(student=st_user, academic_year=academic_year).exists():
                        StudentEnrollment.objects.create(
                            student=st_user,
                            academic_year=academic_year,
                            stream=stream_obj,
                            status='active'
                        )

            # 8. Teacher Assignments
            for stream_key, asg_info in teacher_assignments.items():
                if not isinstance(asg_info, dict):
                    continue
                stream_obj = created_streams.get(str(stream_key).lower()) or created_streams.get(str(stream_key))
                if not stream_obj:
                    parts = str(stream_key).split('-', 1)
                    if len(parts) == 2:
                        stream_obj = Stream.objects.filter(
                            school_class__school=school,
                            school_class__name__iexact=parts[0].strip(),
                            name__iexact=parts[1].strip()
                        ).first()
                if not stream_obj:
                    continue

                class_teacher_val = asg_info.get('classTeacher')
                if class_teacher_val:
                    ct_user = None
                    if isinstance(class_teacher_val, int) or str(class_teacher_val).isdigit():
                        ct_user = User.objects.filter(id=int(class_teacher_val)).first()
                    if not ct_user:
                        ct_user = created_teachers.get(str(class_teacher_val))
                    if ct_user:
                        stream_obj.class_teacher = ct_user
                        stream_obj.save(update_fields=['class_teacher'])

                subjects_map = asg_info.get('subjects', {})
                if isinstance(subjects_map, dict):
                    for sub_name, teacher_val in subjects_map.items():
                        if not teacher_val:
                            continue
                        t_user = None
                        if isinstance(teacher_val, int) or str(teacher_val).isdigit():
                            t_user = User.objects.filter(id=int(teacher_val)).first()
                        if not t_user:
                            t_user = created_teachers.get(str(teacher_val))

                        if t_user:
                            sub_obj = Subject.objects.filter(name__iexact=sub_name).first()
                            if sub_obj:
                                TeacherStreamAssignment.objects.get_or_create(
                                    teacher=t_user,
                                    stream=stream_obj,
                                    subject=sub_obj,
                                    academic_year=academic_year
                                )

        return school

    @staticmethod
    def upload_academic_baseline(school, payload, file_instance, user):
        from .models import AcademicYear, AcademicExamination, AcademicResultSheet
        from django.db import transaction

        academic_year_id = payload.get('academic_year_id')
        term = payload.get('term', 'Term 1')
        exam_type = payload.get('exam_type', 'ENDTERM')

        academic_year = AcademicYear.objects.filter(id=academic_year_id, school=school).first()
        if not academic_year:
            raise ValidationError("Invalid academic year for this school.")

        with transaction.atomic():
            examination, _ = AcademicExamination.objects.get_or_create(
                school=school,
                academic_year=academic_year,
                term=term,
                exam_type=exam_type
            )

            result_sheet = AcademicResultSheet.objects.create(
                examination=examination,
                file=file_instance,
                processing_status='PENDING_REVIEW'
            )

            if school.setup_status in ['PROFILE_COMPLETE', 'STREAMS_CREATED', 'TEACHERS_INVITED', 'SUBJECTS_ASSIGNED', 'STUDENTS_IMPORTED']:
                school.setup_status = 'BASELINE_UPLOADED'
                school.save(update_fields=['setup_status', 'updated_at'])

        return result_sheet

    @staticmethod
    def merge_unverified_school(suggestion_id, target_school_id, actor):
        from .models import UnverifiedSchoolSuggestion, School
        from Resources.models import UserProfile
        from django.db import transaction

        suggestion = UnverifiedSchoolSuggestion.objects.filter(id=suggestion_id).first()
        if not suggestion:
            raise ValidationError("Unverified school suggestion not found.")

        target_school = School.objects.filter(id=target_school_id, is_active=True).first()
        if not target_school:
            raise ValidationError("Target verified school not found.")

        with transaction.atomic():
            # Re-link matching student profiles
            UserProfile.objects.filter(
                unverified_school_name__iexact=suggestion.name
            ).update(
                verified_school=target_school,
                school_association_type='VERIFIED_ORGANIZATION',
                school=target_school.name
            )

            suggestion.status = 'MERGED'
            suggestion.verified_school = target_school
            suggestion.verified_at = timezone.now()
            suggestion.verified_by = actor
            suggestion.save()

        return suggestion

    @staticmethod
    def create_background_task(user, task_type):
        from .models import BackgroundProcessingTask
        return BackgroundProcessingTask.objects.create(
            user=user,
            task_type=task_type,
            status='PENDING',
            progress_percent=0
        )



class BulkUploadService:
    """Handles parsing and importing CSV/Excel files for teacher and student bulk uploads."""

    @staticmethod
    def parse_file(file):
        """Parse an uploaded CSV or Excel file into a list of dicts."""
        import openpyxl
        import csv
        import io
        
        filename = file.name.lower()
        rows = []
        
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            wb = openpyxl.load_workbook(file, read_only=True)
            ws = wb.active
            headers = None
            for i, row in enumerate(ws.iter_rows(values_only=True)):
                if i == 0:
                    headers = [str(h).strip().lower().replace(' ', '_') if h else f'col_{j}' for j, h in enumerate(row)]
                    continue
                if all(cell is None for cell in row):
                    continue
                rows.append(dict(zip(headers, [str(v).strip() if v else '' for v in row])))
            wb.close()
        elif filename.endswith('.csv'):
            content = file.read().decode('utf-8-sig')
            reader = csv.DictReader(io.StringIO(content))
            for row in reader:
                rows.append({k.strip().lower().replace(' ', '_'): v.strip() for k, v in row.items()})
        else:
            raise ValidationError("Unsupported file format. Please upload a CSV or Excel (.xlsx) file.")
        
        return rows

    @staticmethod
    def import_teachers(school, rows):
        """Import teachers from parsed rows. Returns (created_count, errors)."""
        from Resources.models import User, UserProfile
        
        created = []
        errors = []
        
        for i, row in enumerate(rows, start=2):  # start=2 because row 1 is headers
            name = row.get('teacher_name', '') or row.get('name', '')
            phone = row.get('phone_number', '') or row.get('phone', '')
            email = row.get('email', '')
            tsc = row.get('tsc_number', '') or row.get('tsc', '')
            specialties_str = row.get('subject_specialties', '') or row.get('specialties', '')
            
            if not name:
                errors.append({'row': i, 'error': 'Teacher name is required'})
                continue
            if not phone:
                errors.append({'row': i, 'error': 'Phone number is required'})
                continue
            
            # Check for duplicate phone
            if User.objects.filter(phone_number=phone).exists():
                existing_user = User.objects.get(phone_number=phone)
                # Check if already a member of this school
                if OrganizationMembership.objects.filter(user=existing_user, school=school).exists():
                    errors.append({'row': i, 'error': f'Teacher with phone {phone} already exists in this school'})
                    continue
                # Add to school as existing user
                OrganizationMembership.objects.create(
                    user=existing_user, school=school, role='teacher', state='ACTIVE'
                )
                created.append({'row': i, 'name': name, 'status': 'existing_user_added'})
                continue
            
            # Create new user
            names = name.split(' ', 1)
            first_name = names[0]
            last_name = names[1] if len(names) > 1 else ''
            username = f"teacher_{phone.replace('+', '').replace(' ', '')}"
            
            try:
                from django.db import transaction
                with transaction.atomic():
                    user = User.objects.create(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        phone_number=phone,
                        email=email or None,
                        role='teacher',
                        tsc_number=tsc or None,
                    )
                    user.set_password(phone[-6:])  # Default password: last 6 digits of phone
                    user.save()
                    
                    # Create profile
                    UserProfile.objects.get_or_create(user=user)
                    
                    # Create membership
                    OrganizationMembership.objects.create(
                        user=user, school=school, role='teacher', state='ACTIVE'
                    )
                    
                    # Create specialties
                    if specialties_str:
                        from curriculum.models import Subject
                        for spec_name in specialties_str.split(','):
                            spec_name = spec_name.strip()
                            subject = Subject.objects.filter(name__iexact=spec_name).first()
                            if subject:
                                TeacherSpecialty.objects.get_or_create(
                                    teacher=user, subject=subject, school=school
                                )
                
                created.append({'row': i, 'name': name, 'status': 'created'})
            except Exception as e:
                errors.append({'row': i, 'error': str(e)})
        
        return created, errors

    @staticmethod
    def import_students(school, stream, academic_year, rows):
        """Import students from parsed rows into a specific stream. Returns (created_count, errors)."""
        from Resources.models import User, UserProfile
        
        created = []
        errors = []
        
        for i, row in enumerate(rows, start=2):
            name = row.get('student_name', '') or row.get('name', '')
            adm_no = row.get('admission_number', '') or row.get('adm_no', '') or row.get('admission_no', '')
            
            if not name:
                errors.append({'row': i, 'error': 'Student name is required'})
                continue
            if not adm_no:
                errors.append({'row': i, 'error': 'Admission number is required'})
                continue
            
            # Check duplicate admission number within this school
            existing_enrollment = StudentEnrollment.objects.filter(
                stream__school_class__school=school,
                student__admission_number=adm_no
            ).first()
            if existing_enrollment:
                errors.append({'row': i, 'error': f'Admission number {adm_no} already exists in this school'})
                continue
            
            names = name.split(' ', 1)
            first_name = names[0]
            last_name = names[1] if len(names) > 1 else ''
            username = f"student_{school.id}_{adm_no}"
            
            try:
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    admission_number=adm_no,
                    role='student',
                )
                user.set_password(adm_no)  # Default password: admission number
                user.save()
                
                UserProfile.objects.get_or_create(user=user)
                
                OrganizationMembership.objects.create(
                    user=user, school=school, role='student', state='ACTIVE'
                )
                
                StudentEnrollment.objects.create(
                    student=user, stream=stream, academic_year=academic_year, status='active'
                )
                
                created.append({'row': i, 'name': name, 'adm_no': adm_no, 'status': 'created'})
            except Exception as e:
                errors.append({'row': i, 'error': str(e)})
        
        return created, errors
