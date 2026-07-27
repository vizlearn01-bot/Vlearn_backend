from rest_framework import serializers
from django.contrib.auth import get_user_model
from organizations.models import (
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
from curriculum.models import Grade, Subject
from subscriptions.models import SubscriptionPlan

User = get_user_model()


class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']
        read_only_fields = fields


class SchoolSubscriptionSerializer(serializers.ModelSerializer):
    plan_name = serializers.ReadOnlyField(source='plan.name')

    class Meta:
        model = SchoolSubscription
        fields = [
            'id',
            'school',
            'plan',
            'plan_name',
            'max_teachers',
            'max_students',
            'start_date',
            'end_date',
            'is_active',
        ]


class SchoolSerializer(serializers.ModelSerializer):
    owner_detail = UserSummarySerializer(source='owner', read_only=True)
    active_subscription = SchoolSubscriptionSerializer(read_only=True)

    class Meta:
        model = School
        fields = [
            'id',
            'name',
            'code',
            'owner',
            'owner_detail',
            'contact_email',
            'phone_number',
            'address',
            'is_active',
            'created_at',
            'updated_at',
            'active_subscription',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class OrganizationMembershipSerializer(serializers.ModelSerializer):
    user_detail = UserSummarySerializer(source='user', read_only=True)
    school_name = serializers.ReadOnlyField(source='school.name')

    class Meta:
        model = OrganizationMembership
        fields = [
            'id',
            'user',
            'user_detail',
            'school',
            'school_name',
            'role',
            'state',
            'joined_at',
            'updated_at',
            'assigned_by',
        ]
        read_only_fields = ['id', 'joined_at', 'updated_at']


class AcademicYearSerializer(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField(source='school.name')

    class Meta:
        model = AcademicYear
        fields = [
            'id',
            'school',
            'school_name',
            'name',
            'start_date',
            'end_date',
            'is_current',
        ]
        read_only_fields = ['id']


class SchoolClassSerializer(serializers.ModelSerializer):
    curriculum_grade_name = serializers.ReadOnlyField(source='curriculum_grade.name')
    school_name = serializers.ReadOnlyField(source='school.name')

    class Meta:
        model = SchoolClass
        fields = [
            'id',
            'school',
            'school_name',
            'curriculum_grade',
            'curriculum_grade_name',
            'name',
            'code',
        ]
        read_only_fields = ['id']


class StreamSerializer(serializers.ModelSerializer):
    class_teacher_detail = UserSummarySerializer(source='class_teacher', read_only=True)
    class_name = serializers.ReadOnlyField(source='school_class.name')
    school_id = serializers.ReadOnlyField(source='school_class.school_id')

    class Meta:
        model = Stream
        fields = [
            'id',
            'school_class',
            'class_name',
            'school_id',
            'name',
            'class_teacher',
            'class_teacher_detail',
        ]
        read_only_fields = ['id']


class TeacherSubjectAssignmentSerializer(serializers.ModelSerializer):
    teacher_detail = UserSummarySerializer(source='teacher', read_only=True)
    subject_name = serializers.ReadOnlyField(source='subject.name')
    school_name = serializers.ReadOnlyField(source='school.name')
    academic_year_name = serializers.ReadOnlyField(source='academic_year.name')

    class Meta:
        model = TeacherSubjectAssignment
        fields = [
            'id',
            'teacher',
            'teacher_detail',
            'school',
            'school_name',
            'subject',
            'subject_name',
            'academic_year',
            'academic_year_name',
        ]
        read_only_fields = ['id']


class TeacherStreamAssignmentSerializer(serializers.ModelSerializer):
    teacher_detail = UserSummarySerializer(source='teacher', read_only=True)
    stream_name = serializers.ReadOnlyField(source='stream.name')
    class_name = serializers.ReadOnlyField(source='stream.school_class.name')
    school_id = serializers.ReadOnlyField(source='stream.school_class.school_id')
    subject_name = serializers.ReadOnlyField(source='subject.name')
    academic_year_name = serializers.ReadOnlyField(source='academic_year.name')

    class Meta:
        model = TeacherStreamAssignment
        fields = [
            'id',
            'teacher',
            'teacher_detail',
            'stream',
            'stream_name',
            'class_name',
            'school_id',
            'subject',
            'subject_name',
            'academic_year',
            'academic_year_name',
        ]
        read_only_fields = ['id']


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    student_detail = UserSummarySerializer(source='student', read_only=True)
    stream_name = serializers.ReadOnlyField(source='stream.name')
    class_name = serializers.ReadOnlyField(source='stream.school_class.name')
    school_id = serializers.ReadOnlyField(source='stream.school_class.school_id')
    school_name = serializers.ReadOnlyField(source='stream.school_class.school.name')
    academic_year_name = serializers.ReadOnlyField(source='academic_year.name')

    class Meta:
        model = StudentEnrollment
        fields = [
            'id',
            'student',
            'student_detail',
            'stream',
            'stream_name',
            'class_name',
            'school_id',
            'school_name',
            'academic_year',
            'academic_year_name',
            'status',
            'enrolled_at',
        ]
        read_only_fields = ['id', 'enrolled_at']


class SchoolInvitationSerializer(serializers.ModelSerializer):
    raw_token = serializers.CharField(read_only=True)
    school_name = serializers.ReadOnlyField(source='school.name')
    created_by_detail = UserSummarySerializer(source='created_by', read_only=True)

    class Meta:
        model = SchoolInvitation
        fields = [
            'id',
            'email',
            'school',
            'school_name',
            'role',
            'intended_class',
            'intended_stream',
            'intended_subject',
            'invitation_type',
            'token_hash',
            'raw_token',
            'created_by',
            'created_by_detail',
            'created_at',
            'expires_at',
            'state',
        ]
        read_only_fields = ['id', 'token_hash', 'created_by', 'created_at', 'expires_at', 'state']
