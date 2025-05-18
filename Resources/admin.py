from django.contrib import admin
from django import forms
from .models import (
    Category, ExperimentVideo, User, UserProfile, VideoInteraction, Answer, Question, 
    Quiz, QuestionAttempt, StudentAnswer, UserSubscription, SubscriptionPlan, MpesaPayment, 
    AccessToken, UploadedFile
)

# Register models
admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(VideoInteraction)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(QuestionAttempt)
admin.site.register(StudentAnswer)
admin.site.register(UserSubscription)
admin.site.register(SubscriptionPlan)
admin.site.register(MpesaPayment)
admin.site.register(AccessToken)
admin.site.register(UploadedFile)

# Simplified form: only input Cloudflare video ID manually
class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = ExperimentVideo
        fields = '__all__'

class VideoUploadAdmin(admin.ModelAdmin):
    form = VideoUploadForm
    list_display = ['title', 'cloudflare_video_id', 'updated_at']

# Register modified admin
admin.site.register(ExperimentVideo, VideoUploadAdmin)
