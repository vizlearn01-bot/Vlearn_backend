from django.db import models
from django.conf import settings


class School(models.Model):
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
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )
    plan = models.ForeignKey(
        'subscriptions.SubscriptionPlan',
        on_delete=models.PROTECT,
        related_name="school_subscriptions"
    )
    max_teachers = models.PositiveIntegerField(default=10)
    max_students = models.PositiveIntegerField(default=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.school.name} Subscription - {self.plan.name}"


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
