from django.contrib import admin
from .models import Category, VideoCourse, User, UserProfile

admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
@admin.register(VideoCourse)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'difficulty', 'rating', 'created_at')
