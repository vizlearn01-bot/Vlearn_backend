from django.contrib import admin
from .models import Category, ExperimentVideo, User, UserProfile, VideoInteractions, Answer, Question, Quizzes

admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
# admin.site.register(ExperimentVideo)
admin.site.register(VideoInteractions)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quizzes)

@admin.register(ExperimentVideo)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'difficulty', 'rating', 'created_at')
