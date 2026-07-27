from django.contrib import admin
from .models import (
    School,
    OrganizationMembership,
    AcademicYear,
    SchoolClass,
    Stream,
    TeacherSubjectAssignment,
    TeacherStreamAssignment,
    StudentEnrollment,
    SchoolSubscription,
    SchoolInvitation,
)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'owner', 'contact_email', 'phone_number', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'code', 'contact_email', 'owner__username', 'owner__email')


@admin.register(OrganizationMembership)
class OrganizationMembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'school', 'role', 'state', 'joined_at', 'assigned_by')
    list_filter = ('role', 'state', 'joined_at', 'school')
    search_fields = ('user__username', 'user__email', 'school__name', 'school__code')


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'name', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'school')
    search_fields = ('name', 'school__name')


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'name', 'code', 'curriculum_grade')
    list_filter = ('school', 'curriculum_grade')
    search_fields = ('name', 'code', 'school__name')


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_class', 'name', 'class_teacher')
    list_filter = ('school_class__school', 'school_class')
    search_fields = ('name', 'school_class__name', 'class_teacher__username')


@admin.register(TeacherSubjectAssignment)
class TeacherSubjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'school', 'subject', 'academic_year')
    list_filter = ('school', 'academic_year', 'subject')
    search_fields = ('teacher__username', 'teacher__email', 'school__name', 'subject__name')


@admin.register(TeacherStreamAssignment)
class TeacherStreamAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'stream', 'subject', 'academic_year')
    list_filter = ('academic_year', 'subject', 'stream__school_class__school')
    search_fields = ('teacher__username', 'stream__name', 'subject__name')


@admin.register(StudentEnrollment)
class StudentEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'stream', 'academic_year', 'status', 'enrolled_at')
    list_filter = ('status', 'academic_year', 'stream__school_class__school')
    search_fields = ('student__username', 'student__email', 'stream__name')


@admin.register(SchoolSubscription)
class SchoolSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'plan', 'max_teachers', 'max_students', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'plan', 'school')
    search_fields = ('school__name', 'plan__name')


@admin.register(SchoolInvitation)
class SchoolInvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'school', 'role', 'state', 'invitation_type', 'expires_at', 'created_by')
    list_filter = ('role', 'state', 'invitation_type', 'school')
    search_fields = ('email', 'school__name', 'created_by__username')
