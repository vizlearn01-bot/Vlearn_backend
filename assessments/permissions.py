from rest_framework import permissions

class CanEnterMarks(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True
        return True

class CanViewMarks(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True
        return True
