from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
import os

# Base model for shared fields
class BaseVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = CloudinaryField('video', resource_type='video', folder='videos')  
    cover_image = CloudinaryField('image', folder='cover_images', null=True)  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Ensure this model is not created as a database table

    def __str__(self):
        return self.title

# Video Model (all videos stored in one place)
class Video(BaseVideo):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='videos')
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title