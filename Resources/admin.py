from django.contrib import admin
from .models import Video, Category, VideoCourse

admin.site.register(Video)
admin.site.register(Category)

@admin.register(VideoCourse)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'difficulty', 'rating', 'created_at')
