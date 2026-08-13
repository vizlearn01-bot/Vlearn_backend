from rest_framework.permissions import BasePermission
from .policies import user_can

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return user_can(request.user, 'read_curriculum')

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated or not request.user.is_active:
            return False
        role = getattr(request.user, 'role', 'student')
        return role in ['teacher', 'platform_admin'] or request.user.is_superuser

class IsSchoolAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated or not request.user.is_active:
            return False
        role = getattr(request.user, 'role', 'student')
        return role in ['school_admin', 'platform_admin'] or request.user.is_superuser

class IsPlatformAdmin(BasePermission):
    def has_permission(self, request, view):
        return user_can(request.user, 'read_all_users')

class CanCreateInvitation(BasePermission):
    def has_permission(self, request, view):
        return user_can(request.user, 'create_invitation')

class CanWriteContent(BasePermission):
    def has_permission(self, request, view):
        return user_can(request.user, 'write_content')

class HasSimulationAccess(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        from organizations.services import EntitlementService
        if EntitlementService.has_full_curriculum_access(request.user):
            return True
        allowed_subjects = EntitlementService.get_allowed_subject_ids(request.user)
        return len(allowed_subjects) > 0

class HasActiveSubscription(BasePermission):
    """
    Checks if the user has an active subscription to access premium curriculum resources.
    Integrates with EntitlementService to support:
    - Student personal subscriptions
    - Institutional subscriptions (Teacher & Student)
    - Platform/School admin, Teacher, and Superuser bypass
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser or request.user.is_staff or getattr(request.user, 'role', None) in ['teacher', 'platform_admin', 'school_admin']:
            return True
        from organizations.services import EntitlementService
        if EntitlementService.has_full_curriculum_access(request.user):
            return True
        allowed_subjects = EntitlementService.get_allowed_subject_ids(request.user)
        return len(allowed_subjects) > 0

