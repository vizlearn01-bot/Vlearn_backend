from django.contrib import admin
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

@admin.register(ExperimentVideo)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'difficulty', 'rating', 'created_at')
