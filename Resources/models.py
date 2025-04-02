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


class ExperimentVideo(models.Model):
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
    
class VideoInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    video_url = models.URLField(max_length=500, null=False, default=False)  # Store the video URL
    watched_duration = models.IntegerField(default=0)  
    is_completed = models.BooleanField(default=False)
    last_watched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.video_url}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
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

# this model contains questions for a specific video
class Quiz(models.Model):
    video = models.ForeignKey(ExperimentVideo, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    question_count = models.IntegerField(blank=True, null=True)
    difficulty = models.TextField(default='Beginner')
    time_limit = models.IntegerField(default=30) 

    def __str__(self):
        return self.title
    
#this model contains individual questions in the specific video   
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text= models.TextField()
    question_type = models.CharField(max_length=20, choices=[("MCQ", "Multiple Choice"), ("TEXT", "Text Answer")],  default="MCQ" )
    points = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class QuestionAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

class StudentAnswer(models.Model):
    attempt = models.ForeignKey(QuestionAttempt, on_delete=models.CASCADE, related_name='student_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    text_answer = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    points_earned = models.FloatField(default=0)
