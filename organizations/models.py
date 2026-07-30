from django.db import models
from django.conf import settings


import uuid

class School(models.Model):
    SCHOOL_TYPE_CHOICES = (
        ('NATIONAL', 'National School'),
        ('EXTRA_COUNTY', 'Extra County School'),
        ('COUNTY', 'County School'),
        ('SUB_COUNTY', 'Sub County School'),
        ('PRIVATE', 'Private School'),
        ('INTERNATIONAL', 'International School'),
        ('ADULT_LEARNING', 'Adult Learner / Alternative'),
        ('OTHER', 'Other / Not Sure'),
    )

    OWNERSHIP_CHOICES = (
        ('PUBLIC', 'Public'),
        ('PRIVATE', 'Private'),
        ('FAITH_BASED', 'Faith-Based'),
        ('COMMUNITY', 'Community'),
        ('NGO', 'NGO'),
        ('OTHER', 'Other'),
    )

    CURRICULA_CHOICES = (
        ('CBC', 'CBC'),
        ('8-4-4', '8-4-4'),
        ('BOTH', 'Both CBC and 8-4-4'),
    )

    INTERNET_CHOICES = (
        ('RELIABLE', 'Reliable'),
        ('LIMITED', 'Limited'),
        ('NONE', 'None'),
    )

    ELECTRICITY_CHOICES = (
        ('RELIABLE', 'Reliable'),
        ('OCCASIONAL_OUTAGES', 'Occasional Outages'),
        ('FREQUENT_OUTAGES', 'Frequent Outages'),
    )

    SETUP_STATUS_CHOICES = (
        ('PROFILE_COMPLETE', 'Profile Complete'),
        ('STREAMS_CREATED', 'Streams Created'),
        ('TEACHERS_INVITED', 'Teachers Invited'),
        ('SUBJECTS_ASSIGNED', 'Subjects Assigned'),
        ('STUDENTS_IMPORTED', 'Students Imported'),
        ('BASELINE_UPLOADED', 'Baseline Uploaded'),
        ('FULLY_CONFIGURED', 'Fully Configured'),
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_schools"
    )
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    
    # M4 Onboarding Classifications & Infrastructure
    school_type = models.CharField(max_length=30, choices=SCHOOL_TYPE_CHOICES, default='PUBLIC')
    ownership_type = models.CharField(max_length=30, choices=OWNERSHIP_CHOICES, default='PUBLIC')
    curricula_offered = models.CharField(max_length=20, choices=CURRICULA_CHOICES, default='BOTH')
    estimated_students = models.PositiveIntegerField(default=0)
    estimated_teachers = models.PositiveIntegerField(default=0)
    internet_access = models.CharField(max_length=20, choices=INTERNET_CHOICES, default='LIMITED')
    electricity_reliability = models.CharField(max_length=30, choices=ELECTRICITY_CHOICES, default='RELIABLE')
    available_devices = models.JSONField(default=list, blank=True, help_text="List of available device types")
    
    # Location Hierarchy
    location_county = models.CharField(max_length=100, blank=True)
    location_subcounty = models.CharField(max_length=100, blank=True)
    location_ward = models.CharField(max_length=100, blank=True)
    
    # Setup Hub Versioning & Resumable Draft
    onboarding_version = models.IntegerField(default=1)
    setup_status = models.CharField(max_length=30, choices=SETUP_STATUS_CHOICES, default='PROFILE_COMPLETE')
    setup_draft_data = models.JSONField(default=dict, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    completed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='completed_school_setups')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    @property
    def active_subscription(self):
        return self.subscriptions.filter(is_active=True).first()


class OrganizationMembership(models.Model):
    ROLE_CHOICES = [
        ('school_admin', 'School Administrator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    STATE_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('ACTIVE', 'Active'),
        ('SUSPENDED', 'Suspended'),
        ('ARCHIVED', 'Archived'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="memberships"
    )
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="memberships"
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='PENDING')
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_memberships"
    )

    class Meta:
        unique_together = ('user', 'school')
        indexes = [
            models.Index(fields=['school', 'state'], name='org_membership_school_stat_idx'),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.school.name} ({self.get_role_display()}, {self.state})"


class AcademicYear(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="academic_years"
    )
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.school.name} - {self.name}"

    def save(self, *args, **kwargs):
        if self.is_current:
            AcademicYear.objects.filter(school=self.school).exclude(pk=self.pk).update(is_current=False)
        super().save(*args, **kwargs)


class SchoolClass(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="classes"
    )
    curriculum_grade = models.ForeignKey(
        'curriculum.Grade',
        on_delete=models.PROTECT,
        related_name="school_classes"
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.school.name} - {self.name}"


class Stream(models.Model):
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        related_name="streams"
    )
    name = models.CharField(max_length=100)
    class_teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="supervised_streams"
    )

    def __str__(self):
        return f"{self.school_class.name} - {self.name}"


class TeacherSubjectAssignment(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="subject_assignments"
    )
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="teacher_subject_assignments"
    )
    subject = models.ForeignKey(
        'curriculum.Subject',
        on_delete=models.CASCADE,
        related_name="teacher_assignments"
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name="teacher_subject_assignments"
    )

    class Meta:
        unique_together = ('teacher', 'subject', 'academic_year')

    def __str__(self):
        return f"{self.teacher.username} -> {self.subject.name} ({self.academic_year.name})"


class TeacherStreamAssignment(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="stream_assignments"
    )
    stream = models.ForeignKey(
        Stream,
        on_delete=models.CASCADE,
        related_name="teacher_stream_assignments"
    )
    subject = models.ForeignKey(
        'curriculum.Subject',
        on_delete=models.CASCADE,
        related_name="teacher_stream_assignments"
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name="teacher_stream_assignments"
    )

    class Meta:
        unique_together = ('teacher', 'stream', 'subject', 'academic_year')

    def __str__(self):
        return f"{self.teacher.username} -> {self.stream} ({self.subject.name})"


class StudentEnrollment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('transferred', 'Transferred'),
        ('graduated', 'Graduated'),
        ('inactive', 'Inactive'),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="school_enrollments"
    )
    stream = models.ForeignKey(
        Stream,
        on_delete=models.CASCADE,
        related_name="student_enrollments"
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name="student_enrollments"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'academic_year')

    def __str__(self):
        return f"{self.student.username} enrolled in {self.stream} ({self.academic_year.name})"


class SchoolSubscription(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        related_name="subscriptions"
    )
    plan = models.ForeignKey(
        'subscriptions.SubscriptionPlan',
        on_delete=models.PROTECT,
        related_name="school_subscriptions",
        null=True,
        blank=True,
    )
    product_variant = models.ForeignKey(
        'subscriptions.ProductVariant',
        on_delete=models.PROTECT,
        related_name="school_subscriptions",
        null=True,
        blank=True,
    )
    max_teachers = models.PositiveIntegerField(default=10)
    max_students = models.PositiveIntegerField(default=500)
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.PROTECT,
        related_name="school_subscriptions",
        null=True,
        blank=True
    )
    term_name = models.CharField(max_length=50, default="Term 1")
    covered_subjects = models.ManyToManyField(
        'curriculum.Subject',
        related_name="school_subscriptions",
        blank=True
    )
    covered_streams = models.ManyToManyField(
        Stream,
        related_name="school_subscriptions",
        blank=True
    )
    stream_count = models.PositiveIntegerField(default=1)
    agreed_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    invoice = models.OneToOneField(
        'billing_payment.Invoice',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="school_subscription"
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        plan_name = self.product_variant.name if self.product_variant else (self.plan.name if self.plan else "Unknown")
        return f"{self.school.name} Subscription - {plan_name}"


class SchoolInvitation(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('school_admin', 'School Administrator'),
    ]

    STATE_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('EXPIRED', 'Expired'),
        ('REVOKED', 'Revoked'),
    ]

    email = models.EmailField()
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="invitations"
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    intended_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="intended_invitations"
    )
    intended_stream = models.ForeignKey(
        Stream,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="intended_invitations"
    )
    intended_subject = models.ForeignKey(
        'curriculum.Subject',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="intended_invitations"
    )
    invitation_type = models.CharField(max_length=50, default='teacher_invite')
    token_hash = models.CharField(max_length=64, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_school_invitations"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='PENDING')

    def __str__(self):
        return f"Invite for {self.email} to {self.school.name} ({self.role})"


class UnverifiedSchoolSuggestion(models.Model):
    STATUS_CHOICES = (
        ('UNVERIFIED', 'Unverified'),
        ('VERIFIED', 'Verified'),
        ('MERGED', 'Merged'),
        ('ARCHIVED', 'Archived'),
    )

    name = models.CharField(max_length=255)
    county = models.CharField(max_length=100, blank=True)
    sub_county = models.CharField(max_length=100, blank=True)
    proposed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='proposed_schools')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='UNVERIFIED')
    verified_school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True, related_name='suggestions_merged')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_school_suggestions')

    def __str__(self):
        return f"Suggested School: {self.name} [{self.status}]"


class AcademicExamination(models.Model):
    EXAM_TYPE_CHOICES = (
        ('OPENER', 'Opener Exam'),
        ('MIDTERM', 'Midterm Exam'),
        ('ENDTERM', 'End Term Exam'),
        ('MOCK', 'Mock Exam'),
    )

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='examinations')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='examinations')
    term = models.CharField(max_length=50, help_text="e.g., Term 1, Term 2")
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES, default='ENDTERM')
    exam_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.school.name} - {self.term} {self.get_exam_type_display()} ({self.academic_year.name})"


class AcademicResultSheet(models.Model):
    STATUS_CHOICES = (
        ('PENDING_REVIEW', 'Pending Review'),
        ('PROCESSING', 'Processing'),
        ('PARSED', 'Parsed'),
        ('FAILED', 'Failed'),
    )

    examination = models.ForeignKey(AcademicExamination, on_delete=models.CASCADE, related_name='result_sheets')
    file = models.ForeignKey('Resources.UploadedFile', on_delete=models.CASCADE, related_name='academic_result_sheets')
    processing_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='PENDING_REVIEW')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result Sheet {self.file.name} for {self.examination}"


class BackgroundProcessingTask(models.Model):
    TASK_TYPE_CHOICES = (
        ('STUDENT_IMPORT', 'Student Roster Import'),
        ('EXAM_UPLOAD', 'Exam Result Sheet Upload'),
    )

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )

    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    celery_task_id = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='background_tasks')
    task_type = models.CharField(max_length=30, choices=TASK_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    progress_percent = models.PositiveIntegerField(default=0)
    error_log = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Task {self.task_type} ({self.status}) - {self.progress_percent}%"
