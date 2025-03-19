from django.contrib import admin
from .models import Category, ExperimentVideo, User, UserProfile

admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
# admin.site.register(ExperimentVideo)

@admin.register(ExperimentVideo)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'difficulty', 'rating', 'created_at')
