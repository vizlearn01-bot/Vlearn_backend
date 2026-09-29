from rest_framework import permissions

class CanEnterMarks(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True
        user_role = getattr(request.user, 'role', None)
        if user_role in ['teacher', 'school_admin']:
            return True
        if hasattr(request.user, 'memberships'):
            return request.user.memberships.filter(
                role__in=['teacher', 'school_admin'],
                state__in=['ACCEPTED', 'ACTIVE']
            ).exists()
        return False

class CanViewMarks(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True
        return True
