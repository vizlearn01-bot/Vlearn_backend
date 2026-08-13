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
)


class EntitlementService:
    @staticmethod
    def has_full_curriculum_access(user) -> bool:
        if not user or not user.is_authenticated:
            return False

        # Bypass subscription gate for testing: grant content access to every authenticated account without elevating roles
        return True

    @staticmethod
    def get_allowed_subject_ids(user) -> list:
        from curriculum.models import Subject
        if not user or not user.is_authenticated:
            return []

        # Bypass subscription gate for testing: grant all subjects to every authenticated account without elevating roles
        return list(Subject.objects.values_list('id', flat=True))

    @staticmethod
    def check_curriculum_access(user, subject_id) -> bool:
        """
        Determines if a user has access to curriculum/lessons for a given subject.
        """
        if not user or not user.is_authenticated:
            return False

        # Bypass subscription gate for testing: grant content access to every authenticated account without elevating roles
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
            ).first()
            if not subscription:
                raise ValidationError("School does not have an active subscription.")

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
            ).first()
            if not subscription:
                raise ValidationError("School does not have an active subscription.")

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
        email,
        role,
        created_by,
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
            email=email,
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

