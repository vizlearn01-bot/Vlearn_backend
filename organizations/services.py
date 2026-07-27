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
        if getattr(user, 'role', None) == 'platform_admin' or user.is_superuser:
            return True

        now = timezone.now()

        # 2. Personal Subscription
        if hasattr(user, 'has_active_personal_subscription') and callable(user.has_active_personal_subscription):
            if user.has_active_personal_subscription():
                return True

        # Check Subscription / UserSubscription models
        try:
            from subscriptions.models import Subscription
            if Subscription.objects.filter(
                user=user,
                is_active=True
            ).filter(Q(end_date__isnull=True) | Q(end_date__gte=now)).exists():
                return True
        except ImportError:
            pass

        try:
            from Resources.models import UserSubscription
            if UserSubscription.objects.filter(
                user=user,
                is_active=True
            ).filter(Q(end_date__isnull=True) | Q(end_date__gte=now)).exists():
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
        now = timezone.now()
        teacher_assigned = TeacherStreamAssignment.objects.filter(
            teacher=user,
            stream__school_class__school__subscriptions__is_active=True,
            stream__school_class__school__subscriptions__end_date__gte=now,
            stream__school_class__school__memberships__user=user,
            stream__school_class__school__memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).values_list('subject_id', flat=True)

        teacher_subject_assigned = TeacherSubjectAssignment.objects.filter(
            teacher=user,
            school__subscriptions__is_active=True,
            school__subscriptions__end_date__gte=now,
            school__memberships__user=user,
            school__memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).values_list('subject_id', flat=True)

        student_enrolled = StudentEnrollment.objects.filter(
            student=user,
            status='active',
            stream__school_class__school__subscriptions__is_active=True,
            stream__school_class__school__subscriptions__end_date__gte=now,
            stream__school_class__school__memberships__user=user,
            stream__school_class__school__memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).values_list('stream__school_class__curriculum_grade__subjects__id', flat=True)

        return list(set(list(teacher_assigned) + list(teacher_subject_assigned) + list(student_enrolled)))

    @staticmethod
    def check_curriculum_access(user, subject_id) -> bool:
        """
        Determines if a user has access to curriculum/lessons for a given subject.
        Returns True if:
        1. User is platform_admin or superuser.
        2. User has active personal subscription.
        3. User has active school membership with active school subscription and is assigned/enrolled in that subject.
        """
        if not user or not user.is_authenticated:
            return False

        # 1. Platform Admin / Superuser
        if getattr(user, 'role', None) == 'platform_admin' or user.is_superuser:
            return True

        now = timezone.now()

        # 2. Personal Subscription
        if hasattr(user, 'has_active_personal_subscription') and callable(user.has_active_personal_subscription):
            if user.has_active_personal_subscription():
                return True

        # Check Subscription / UserSubscription models
        try:
            from subscriptions.models import Subscription
            if Subscription.objects.filter(
                user=user,
                is_active=True
            ).filter(Q(end_date__isnull=True) | Q(end_date__gte=now)).exists():
                return True
        except ImportError:
            pass

        try:
            from Resources.models import UserSubscription
            if UserSubscription.objects.filter(
                user=user,
                is_active=True
            ).filter(Q(end_date__isnull=True) | Q(end_date__gte=now)).exists():
                return True
        except ImportError:
            pass

        # 3. School Subscription & Assignment / Enrollment
        active_memberships = user.memberships.filter(state__in=['ACCEPTED', 'ACTIVE'])
        if not active_memberships.exists():
            return False

        # Check Teacher assignments
        teacher_assigned = TeacherStreamAssignment.objects.filter(
            teacher=user,
            subject_id=subject_id,
            stream__school_class__school__subscriptions__is_active=True,
            stream__school_class__school__subscriptions__end_date__gte=now,
            stream__school_class__school__memberships__user=user,
            stream__school_class__school__memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).exists() or TeacherSubjectAssignment.objects.filter(
            teacher=user,
            subject_id=subject_id,
            school__subscriptions__is_active=True,
            school__subscriptions__end_date__gte=now,
            school__memberships__user=user,
            school__memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).exists()

        if teacher_assigned:
            return True

        # Check Student enrollment
        student_enrolled = StudentEnrollment.objects.filter(
            student=user,
            status='active',
            stream__school_class__curriculum_grade__subjects__id=subject_id,
            stream__school_class__school__subscriptions__is_active=True,
            stream__school_class__school__subscriptions__end_date__gte=now,
            stream__school_class__school__memberships__user=user,
            stream__school_class__school__memberships__state__in=['ACCEPTED', 'ACTIVE']
        ).exists()

        if student_enrolled:
            return True

        # School Admin check for access in their active school
        is_school_admin = active_memberships.filter(
            role='school_admin',
            school__subscriptions__is_active=True,
            school__subscriptions__end_date__gte=now
        ).exists()

        if is_school_admin:
            return True

        return False

    @staticmethod
    def enforce_teacher_capacity(school) -> None:
        """
        Raises ValidationError if (active teachers + pending teacher invitations) >= subscription.max_teachers.
        """
        subscription = school.active_subscription
        now = timezone.now()
        if not subscription or not subscription.is_active or subscription.end_date < now:
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
        """
        subscription = school.active_subscription
        now = timezone.now()
        if not subscription or not subscription.is_active or subscription.end_date < now:
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
