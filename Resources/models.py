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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = CloudinaryField("image", folder="user_avatars", blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)
    enrolled_courses = models.IntegerField(default=0)
    completed_courses = models.IntegerField(default=0)
    average_score = models.FloatField(default=0.0)
    total_hours = models.FloatField(default=0.0)
    onboarding_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"


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
    file = models.FileField(upload_to="uploads/%Y/%m/%d/")
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

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
