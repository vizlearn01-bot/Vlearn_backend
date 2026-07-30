from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
import os
from django.contrib.auth.models import AbstractUser


# user model
class User(AbstractUser):
    ROLE_STUDENT = 'student'
    ROLE_TEACHER = 'teacher'
    ROLE_SCHOOL_ADMIN = 'school_admin'
    ROLE_PLATFORM_ADMIN = 'platform_admin'

    ROLE_CHOICES = (
        (ROLE_STUDENT, 'Student'),
        (ROLE_TEACHER, 'Teacher'),
        (ROLE_SCHOOL_ADMIN, 'School Administrator'),
        (ROLE_PLATFORM_ADMIN, 'Platform Administrator'),
    )

    ACCOUNT_ACTIVE = 'ACTIVE'
    ACCOUNT_PENDING = 'PENDING'
    ACCOUNT_STATE_CHOICES = [(ACCOUNT_ACTIVE, 'Active'), (ACCOUNT_PENDING, 'Pending')]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_STUDENT)
    account_state = models.CharField(max_length=20, choices=ACCOUNT_STATE_CHOICES, default=ACCOUNT_ACTIVE)
    # Architecture Note: Temporary IntegerField, superseded by OrganizationMembership in future sprint
    organization_id = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.role == self.ROLE_PLATFORM_ADMIN:
            self.is_staff = True
        super().save(*args, **kwargs)



class UserProfile(models.Model):
    ONBOARDING_STATUS_CHOICES = (
        ('NOT_STARTED', 'Not Started'),
        ('IN_PROGRESS', 'In Progress'),
        ('MINIMUM_COMPLETE', 'Minimum Complete'),
        ('FULLY_COMPLETE', 'Fully Complete'),
    )

    SCHOOL_ASSOCIATION_CHOICES = (
        ('VERIFIED_ORGANIZATION', 'Verified Organization'),
        ('UNVERIFIED_SUGGESTION', 'Unverified Suggestion'),
        ('INDEPENDENT', 'Independent / No Association'),
        ('NONE', 'None'),
    )

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

    CONFIDENCE_CHOICES = (
        ('VERY_CONFIDENT', 'Very Confident'),
        ('CONFIDENT', 'Confident'),
        ('AVERAGE', 'Average'),
        ('NEED_SUPPORT', 'Need More Support'),
    )

    DEVICE_CHOICES = (
        ('PERSONAL_PHONE', 'Personal Phone'),
        ('TABLET', 'Tablet'),
        ('LAPTOP', 'Laptop'),
        ('SHARED_FAMILY_COMPUTER', 'Shared Family Computer'),
        ('PARENT_GUARDIAN_DEVICE', 'Parent / Guardian Device'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = CloudinaryField("image", folder="user_avatars", blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)
    curriculum = models.ForeignKey('curriculum.Curriculum', on_delete=models.SET_NULL, null=True, blank=True, related_name='student_profiles')
    curriculum_grade = models.ForeignKey('curriculum.Grade', on_delete=models.SET_NULL, null=True, blank=True, related_name='student_profiles')
    selected_subjects = models.ManyToManyField('curriculum.Subject', blank=True, related_name='selected_by_students')
    
    # M4 Onboarding Enhancements
    onboarding_version = models.IntegerField(default=1, help_text="Version of onboarding completed")
    onboarding_status = models.CharField(max_length=30, choices=ONBOARDING_STATUS_CHOICES, default='NOT_STARTED')
    location_county = models.CharField(max_length=100, blank=True)
    location_subcounty = models.CharField(max_length=100, blank=True)
    location_town_village = models.CharField(max_length=100, blank=True)
    school_association_type = models.CharField(max_length=30, choices=SCHOOL_ASSOCIATION_CHOICES, default='NONE')
    unverified_school_name = models.CharField(max_length=255, blank=True, null=True)
    verified_school = models.ForeignKey('organizations.School', on_delete=models.SET_NULL, null=True, blank=True, related_name='associated_student_profiles')
    school_type = models.CharField(max_length=30, choices=SCHOOL_TYPE_CHOICES, default='OTHER')
    confidence_level = models.CharField(max_length=30, choices=CONFIDENCE_CHOICES, default='AVERAGE')
    primary_device = models.CharField(max_length=40, choices=DEVICE_CHOICES, default='PERSONAL_PHONE')
    career_aspiration = models.CharField(max_length=255, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    enrolled_courses = models.IntegerField(default=0)
    completed_courses = models.IntegerField(default=0)
    average_score = models.FloatField(default=0.0)
    total_hours = models.FloatField(default=0.0)
    onboarding_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.onboarding_status})"


class StudentSubjectSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subject_selections')
    subject = models.ForeignKey('curriculum.Subject', on_delete=models.CASCADE, related_name='student_selections')
    is_priority = models.BooleanField(default=False, help_text="Designates if this subject requires support")
    priority_rank = models.PositiveIntegerField(null=True, blank=True, help_text="Rank 1, 2, or 3 for priority")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'subject')
        ordering = ['-is_priority', 'priority_rank', 'subject__name']

    def __str__(self):
        return f"{self.user.username} - {self.subject.name} (Priority: {self.is_priority})"


class StudentAcademicBaseline(models.Model):
    GRADING_SCHEME_CHOICES = (
        ('LETTER_GRADE', 'Letter Grade (A-E)'),
        ('PERCENTAGE', 'Percentage (0-100%)'),
        ('CBC_RUBRIC', 'CBC Rubric (EE, ME, AE, BE)'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='academic_baselines')
    subject = models.ForeignKey('curriculum.Subject', on_delete=models.CASCADE, related_name='student_baselines')
    academic_year = models.ForeignKey('organizations.AcademicYear', on_delete=models.SET_NULL, null=True, blank=True, related_name='student_baselines')
    examination = models.ForeignKey('organizations.AcademicExamination', on_delete=models.SET_NULL, null=True, blank=True, related_name='student_baselines')
    
    grading_scheme = models.CharField(max_length=20, choices=GRADING_SCHEME_CHOICES, default='LETTER_GRADE')
    raw_previous_grade = models.CharField(max_length=20)
    normalized_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    target_grade = models.CharField(max_length=20, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'subject', 'academic_year', 'examination')

    def __str__(self):
        return f"{self.user.username} Baseline - {self.subject.name}: {self.raw_previous_grade}"


# Validator first
@deconstructible
class ValidateImageFileExtension:
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]

    def __call__(self, value):
        ext = os.path.splitext(value.name)[1]
        if ext.lower() not in self.valid_extensions:
            raise ValidationError(
                f'Unsupported file extension. Supported extensions are: {", ".join(self.valid_extensions)}'
            )


# Category model
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField(
        "image", folder="category_images", validators=[ValidateImageFileExtension()]
    )

    def __str__(self):
        return self.title


# models that relate to the video content
class ExperimentVideo(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True)
    image = models.URLField(blank=True)  # Changed to blank=True
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ("Gas Laws", "Gas Laws"),
            ("The Mole", "The Mole"),
            ("Organic Chemistry 1", "Organic Chemistry 1"),
            ("Nitrogen", "Nitrogen"),
            ("Sulphur", "Sulphur"),
            ("Chlorine", "Chlorine"),
        ],
        null=True,
    )
    duration = models.CharField(max_length=50, blank=True)  # Changed to blank=True
    difficulty = models.CharField(
        max_length=50,
        choices=[
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Advanced", "Advanced"),
        ],
    )
    instructor = models.CharField(max_length=255)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, default=0.0
    )  # Added default
    cloudflare_video_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    @property
    def playback_url(self):
        return (
            f"https://videodelivery.net/{self.cloudflare_video_id}/manifest/video.m3u8"
        )


class VideoInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    video_url = models.URLField(
        max_length=500, null=False, default=''
    )  # Store the video URL
    watched_duration = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    last_watched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.video_url}"


# models that relate to subscriptions
class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()  # 30 for monthly, 365 for yearly, etc.
    features = models.JSONField(default=list)
    is_popular = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    mpesa_number = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.plan.name}"


class AccessToken(models.Model):
    token = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "created_at"

    def __str__(self):
        return self.token


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="uploaded_files")
    file = models.FileField(upload_to="uploads/%Y/%m/%d/")
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'file_type'], name='uploadedfile_user_filetype_idx'),
        ]

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        self.size = self.file.size
        self.file_type = self.file.name.split(".")[-1].lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Invitation(models.Model):
    email = models.EmailField()
    role = models.CharField(max_length=20)
    organization_id = models.IntegerField(null=True, blank=True)
    token_hash = models.CharField(max_length=64, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_invitations')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    state = models.CharField(max_length=20, default='pending')
    accepted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='accepted_invitations')

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token_hash = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
