from django.contrib import admin
from .models import Category, ExperimentVideo, User, UserProfile, VideoInteraction, Answer, Question, Quiz

admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(VideoInteraction)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)

@admin.register(ExperimentVideo)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'difficulty', 'rating', 'created_at')
