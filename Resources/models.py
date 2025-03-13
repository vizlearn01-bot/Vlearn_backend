from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
import os
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add custom fields if needed
    pass

# Validator first
@deconstructible
class ValidateImageFileExtension:
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    def __call__(self, value):
        ext = os.path.splitext(value.name)[1]
        if ext.lower() not in self.valid_extensions:
            raise ValidationError(f'Unsupported file extension. Supported extensions are: {", ".join(self.valid_extensions)}')

# Category model second
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image', folder='category_images', validators=[ValidateImageFileExtension()])

    def __str__(self):
        return self.title


class VideoCourse(models.Model):

    title = models.CharField(max_length=255)
    image = models.URLField()
    description = models.TextField()
    duration = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    instructor = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    video_link = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image', folder='user_avatars', blank=True, null=True) 
    phone_number = models.CharField(max_length=15, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)
    enrolled_courses = models.IntegerField(default=0)
    completed_courses = models.IntegerField(default=0)
    average_score = models.FloatField(default=0.0)
    total_hours = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username}'s Profile"
