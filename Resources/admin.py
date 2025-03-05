from django.contrib import admin
from .models import Category, VideoCourse

admin.site.register(Category)

@admin.register(VideoCourse)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'difficulty', 'rating', 'created_at')
