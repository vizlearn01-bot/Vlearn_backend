from django.contrib import admin
from .models import Category, VideoCourse, User

admin.site.register(Category)
admin.site.register(User)

@admin.register(VideoCourse)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'difficulty', 'rating', 'created_at')
