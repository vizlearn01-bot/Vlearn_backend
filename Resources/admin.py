from django.contrib import admin
from django import forms
import requests
from django.conf import settings
from .models import (Category, ExperimentVideo, User, UserProfile, VideoInteraction, Answer, Question, 
Quiz, QuestionAttempt, StudentAnswer, UserSubscription, SubscriptionPlan, MpesaPayment, AccessToken, UploadedFile)

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

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = ExperimentVideo
        fields = ['title']

    video_file = forms.FileField()

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Upload to Cloudflare Stream
        headers = {
            "Authorization": f"Bearer {settings.CLOUDFLARE_STREAM_AUTH_TOKEN}"
        }

        upload_url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CLOUDFLARE_STREAM_ACCOUNT_ID}/stream"

        file = self.files['video_file']
        files = {
            'file': (file.name, file.read()),
        }

        response = requests.post(upload_url, headers=headers, files=files)
        data = response.json()

        if not data.get('success'):
            raise forms.ValidationError("Failed to upload to Cloudflare Stream")

        instance.cloudflare_video_id = data['result']['uid']

        if commit:
            instance.save()
        return instance

class videoupload(admin.ModelAdmin):
    form = VideoUploadForm
    list_display = ['title', 'cloudflare_video_id', 'updated_at']

admin.site.register(ExperimentVideo, videoupload)