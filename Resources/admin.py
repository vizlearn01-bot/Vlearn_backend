from django.contrib import admin
from .models import Video, Categories

# Register each form-level video model separately
@admin.register(Video)

# Register the Categories model
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
