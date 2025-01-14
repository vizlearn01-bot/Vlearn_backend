from django.contrib import admin
from .models import Video, Category

# Register each form-level video model separately
@admin.register(Video)

# Register the Categories model
@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
