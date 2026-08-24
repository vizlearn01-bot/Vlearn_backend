from rest_framework.permissions import BasePermission
from django.utils import timezone


def get_school_from_obj_or_request(request, view, obj=None):
    """
    Helper utility to resolve the target School instance from a request, view, or object.
    """
    if obj is not None:
        if hasattr(obj, 'school'):
            return obj.school
        elif hasattr(obj, 'school_class') and hasattr(obj.school_class, 'school'):
            return obj.school_class.school
        elif hasattr(obj, 'stream') and hasattr(obj.stream, 'school_class'):
            return obj.stream.school_class.school

    school_id = request.parser_context.get('kwargs', {}).get('school_id') or request.query_params.get('school_id')
    if school_id:
        from organizations.models import School
        return School.objects.filter(pk=school_id).first()
    return None


class IsSchoolAdmin(BasePermission):
    """
    Permission check for School Administrators.
    Grants access if request.user has ACTIVE or ACCEPTED school_admin membership for the school
    (or is platform_admin / superuser).
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True

        school = get_school_from_obj_or_request(request, view)
        if school:
            return request.user.memberships.filter(
                school=school,
                role='school_admin',
                state__in=['ACCEPTED', 'ACTIVE']
            ).exists()

        return request.user.memberships.filter(
            role='school_admin',
            state__in=['ACCEPTED', 'ACTIVE']
        ).exists()

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True

        school = get_school_from_obj_or_request(request, view, obj)
        if not school:
            return False

        return request.user.memberships.filter(
            school=school,
            role='school_admin',
            state__in=['ACCEPTED', 'ACTIVE']
        ).exists()


class IsSchoolTeacher(BasePermission):
    """
    Permission check for Teachers in a school.
    Grants access if request.user is an ACTIVE or ACCEPTED teacher in the school (or platform_admin / superuser).
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True

        school = get_school_from_obj_or_request(request, view)
        if school:
            return request.user.memberships.filter(
                school=school,
                role='teacher',
                state__in=['ACCEPTED', 'ACTIVE']
            ).exists()

        return request.user.memberships.filter(
            role='teacher',
            state__in=['ACCEPTED', 'ACTIVE']
        ).exists()

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True

        school = get_school_from_obj_or_request(request, view, obj)
        if not school:
            return False

        return request.user.memberships.filter(
            school=school,
            role='teacher',
            state__in=['ACCEPTED', 'ACTIVE']
        ).exists()


class IsSchoolStudent(BasePermission):
    """
    Permission check for Students in a school.
    Grants access if request.user is an ACTIVE or ACCEPTED student in the school (or platform_admin / superuser).
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True

        school = get_school_from_obj_or_request(request, view)
        if school:
            return request.user.memberships.filter(
                school=school,
                role='student',
                state__in=['ACCEPTED', 'ACTIVE']
            ).exists()

        return request.user.memberships.filter(
            role='student',
            state__in=['ACCEPTED', 'ACTIVE']
        ).exists()

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        if getattr(request.user, 'role', None) == 'platform_admin' or request.user.is_superuser:
            return True

        school = get_school_from_obj_or_request(request, view, obj)
        if not school:
            return False

        return request.user.memberships.filter(
            school=school,
            role='student',
            state__in=['ACCEPTED', 'ACTIVE']
        ).exists()


class HasActiveSchoolSubscription(BasePermission):
    """
    Permission check to verify if the school associated with request or object has an active subscription.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        role = getattr(request.user, 'role', None)
        if role in ['platform_admin', 'school_admin', 'teacher'] or request.user.is_superuser or request.user.is_staff:
            return True

        from organizations.models import SchoolSubscription

        school = get_school_from_obj_or_request(request, view)
        now = timezone.now()
        if school:
            return SchoolSubscription.objects.filter(
                school=school,
                is_active=True,
                end_date__gte=now
            ).exists()

        user_schools = request.user.memberships.filter(
            state__in=['ACCEPTED', 'ACTIVE']
        ).values_list('school_id', flat=True)

        return SchoolSubscription.objects.filter(
            school_id__in=user_schools,
            is_active=True,
            end_date__gte=now
        ).exists()

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        role = getattr(request.user, 'role', None)
        if role in ['platform_admin', 'school_admin', 'teacher'] or request.user.is_superuser or request.user.is_staff:
            return True

        from organizations.models import SchoolSubscription

        school = get_school_from_obj_or_request(request, view, obj)
        if not school:
            return False

        now = timezone.now()
        return SchoolSubscription.objects.filter(
            school=school,
            is_active=True,
            end_date__gte=now
        ).exists()
