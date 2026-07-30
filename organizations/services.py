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

        # Only Platform Admins / Superusers / Staff get global bypass
        if getattr(user, 'role', None) == 'platform_admin' or user.is_superuser or user.is_staff:
            return True

        now = timezone.now()

        # Check ProductVariant PLATFORM scope or legacy personal subscription
        try:
            from subscriptions.models import Subscription, AccessScope
            platform_subs = Subscription.objects.filter(
                user=user,
                is_active=True
            ).filter(Q(end_date__isnull=True) | Q(end_date__gte=now))

            for sub in platform_subs:
                if sub.product_variant:
                    if sub.product_variant.access_scopes.filter(scope_type='PLATFORM').exists():
                        return True
                elif sub.plan:
                    # Legacy plan check
                    return True
        except ImportError:
            pass

        # School Admin check for access in their active school
        is_school_admin = user.memberships.filter(
            state__in=['ACCEPTED', 'ACTIVE'],
            role='school_admin',
            school__subscriptions__is_active=True,
            school__subscriptions__end_date__gte=now
        ).exists()

        if is_school_admin:
            return True

        return False

    @staticmethod
    def get_allowed_subject_ids(user) -> list:
        from curriculum.models import Subject
        if not user or not user.is_authenticated:
            return []

        all_subjects = list(Subject.objects.values_list('id', flat=True))

        # Platform Admin / Superuser / Staff get all subjects
        if getattr(user, 'role', None) == 'platform_admin' or user.is_superuser or user.is_staff:
            return all_subjects

        now = timezone.now()
        allowed_subjects = set()

        # 1. Personal Subscriptions (including relational SubscriptionSubject snapshots)
        try:
            from subscriptions.models import Subscription
            user_subs = Subscription.objects.filter(
                user=user,
                is_active=True
            ).filter(Q(end_date__isnull=True) | Q(end_date__gte=now)).select_related('product_variant').prefetch_related('entitled_subjects')

            for sub in user_subs:
                # Snapshotted relational subject entitlements
                snapshotted = list(sub.entitled_subjects.values_list('subject_id', flat=True))
                if snapshotted:
                    allowed_subjects.update(snapshotted)

                if sub.product_variant:
                    for scope in sub.product_variant.access_scopes.all():
                        if scope.scope_type == 'PLATFORM':
                            return all_subjects
                        elif scope.scope_type == 'GRADE' and scope.grade:
                            grade_subj_ids = Subject.objects.filter(grade=scope.grade).values_list('id', flat=True)
                            allowed_subjects.update(grade_subj_ids)
                        elif scope.scope_type == 'SUBJECT' and scope.subject:
                            allowed_subjects.add(scope.subject.id)
                elif sub.plan:
                    # Legacy plan grants all subjects
                    return all_subjects
        except ImportError:
            pass

        # 2. Institutional Student Enrollments (Subject ∩ Stream ∩ Active Term)
        active_student_enrollments = StudentEnrollment.objects.filter(
            student=user,
            status='active',
            stream__school_class__school__memberships__user=user,
            stream__school_class__school__memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).select_related('stream__school_class__school')

        for enrollment in active_student_enrollments:
            school = enrollment.stream.school_class.school
            school_subs = SchoolSubscription.objects.filter(
                school=school,
                is_active=True,
                start_date__lte=now,
                end_date__gte=now
            )
            for sub in school_subs:
                # If specific covered streams are defined, verify enrollment stream is covered
                has_streams = sub.covered_streams.exists()
                if has_streams and not sub.covered_streams.filter(id=enrollment.stream_id).exists():
                    continue

                # Add covered subjects
                covered_sub_ids = list(sub.covered_subjects.values_list('id', flat=True))
                if covered_sub_ids:
                    allowed_subjects.update(covered_sub_ids)
                else:
                    # Fallback for legacy school subs without explicit subject list: grant grade subjects
                    grade_subjs = Subject.objects.filter(grade=enrollment.stream.school_class.curriculum_grade).values_list('id', flat=True)
                    allowed_subjects.update(grade_subjs)

        # 3. Institutional Teacher Assignments (Subject ∩ Stream ∩ Active Term)
        teacher_stream_assigns = TeacherStreamAssignment.objects.filter(
            teacher=user,
            stream__school_class__school__memberships__user=user,
            stream__school_class__school__memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).select_related('stream__school_class__school')

        for assign in teacher_stream_assigns:
            school = assign.stream.school_class.school
            school_subs = SchoolSubscription.objects.filter(
                school=school,
                is_active=True,
                start_date__lte=now,
                end_date__gte=now
            )
            for sub in school_subs:
                has_streams = sub.covered_streams.exists()
                has_subjects = sub.covered_subjects.exists()

                stream_ok = not has_streams or sub.covered_streams.filter(id=assign.stream_id).exists()
                subject_ok = not has_subjects or sub.covered_subjects.filter(id=assign.subject_id).exists()

                if stream_ok and subject_ok:
                    allowed_subjects.add(assign.subject_id)

        teacher_subject_assigns = TeacherSubjectAssignment.objects.filter(
            teacher=user,
            school__memberships__user=user,
            school__memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).select_related('school')

        for assign in teacher_subject_assigns:
            school = assign.school
            school_subs = SchoolSubscription.objects.filter(
                school=school,
                is_active=True,
                start_date__lte=now,
                end_date__gte=now
            )
            for sub in school_subs:
                has_subjects = sub.covered_subjects.exists()
                subject_ok = not has_subjects or sub.covered_subjects.filter(id=assign.subject_id).exists()
                if subject_ok:
                    allowed_subjects.add(assign.subject_id)

        return list(allowed_subjects)

    @staticmethod
    def check_curriculum_access(user, subject_id) -> bool:
        """
        Determines if a user has access to curriculum/lessons for a given subject.
        """
        if not user or not user.is_authenticated:
            return False

        # Platform Admin / Superuser / Staff bypass
        if getattr(user, 'role', None) == 'platform_admin' or user.is_superuser or user.is_staff:
            return True

        if not subject_id:
            return False

        allowed_ids = EntitlementService.get_allowed_subject_ids(user)
        try:
            return int(subject_id) in allowed_ids or str(subject_id) in [str(s) for s in allowed_ids]
        except (ValueError, TypeError):
            return str(subject_id) in [str(s) for s in allowed_ids]

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
        from .models import School, OrganizationMembership
        from django.db import transaction

        name = payload.get('name')
        code = payload.get('code')
        if not name or not code:
            raise ValidationError("School name and code are required.")

        if School.objects.filter(code=code).exists():
            raise ValidationError(f"School code '{code}' is already registered.")

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
                estimated_students=payload.get('estimated_students', 0),
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

