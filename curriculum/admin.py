from django.contrib import admin
from .models import (
    Curriculum, Grade, Subject, Topic,
    Lesson, LessonBlock, LearningUnit,
    KnowledgePack, KnowledgeChunk,
    PedagogyTemplate, GenerationRule, GenerationJob,
)


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'curriculum', 'level')
    search_fields = ('name', 'curriculum__name')
    list_filter = ('curriculum',)
    ordering = ('curriculum', 'level')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade')
    search_fields = ('name', 'grade__name')
    list_filter = ('grade__curriculum', 'grade')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'order')
    search_fields = ('name', 'subject__name')
    list_filter = ('subject__grade', 'subject')
    ordering = ('subject', 'order')


@admin.register(LearningUnit)
class LearningUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'order')
    search_fields = ('name', 'topic__name')
    list_filter = ('topic__subject',)
    ordering = ('topic', 'order')


@admin.register(PedagogyTemplate)
class PedagogyTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'is_active')
    search_fields = ('name', 'subject__name')
    list_filter = ('is_active', 'subject')


@admin.register(GenerationRule)
class GenerationRuleAdmin(admin.ModelAdmin):
    list_display = ('template', 'block_type', 'order', 'is_mandatory')
    search_fields = ('block_type', 'template__name')
    list_filter = ('template', 'is_mandatory')
    ordering = ('template', 'order')


@admin.register(KnowledgePack)
class KnowledgePackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'version', 'status', 'created_at', 'approved_at')
    search_fields = ('subject__name',)
    list_filter = ('status', 'subject')
    ordering = ('subject', '-version')


@admin.register(KnowledgeChunk)
class KnowledgeChunkAdmin(admin.ModelAdmin):
    list_display = ('knowledge_pack', 'chunk_type', 'section_title', 'order')
    search_fields = ('section_title', 'content_text')
    list_filter = ('chunk_type', 'knowledge_pack')
    ordering = ('knowledge_pack', 'order')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'learning_unit', 'version', 'status', 'published_at')
    search_fields = ('topic__name', 'title')
    list_filter = ('status', 'topic__subject')
    ordering = ('topic', '-version')


@admin.register(LessonBlock)
class LessonBlockAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'block_type', 'title', 'order')
    search_fields = ('title', 'lesson__topic__name')
    list_filter = ('block_type', 'lesson__topic')
    ordering = ('lesson', 'order')


@admin.register(GenerationJob)
class GenerationJobAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'job_type', 'status', 'created_at', 'completed_at')
    search_fields = ('lesson__topic__name',)
    list_filter = ('status', 'job_type')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'completed_at', 'error_message')
