from django.contrib import admin
from django.core.cache import cache
from django.utils import timezone
from .models import Article, ArticleCategory, ArticleTag
from .signals import CACHE_KEYS_TO_INVALIDATE


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "linked_subject_name", "order", "created_at"]
    list_filter = ["linked_subject_name"]
    search_fields = ["name", "linked_subject_name", "description"]
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["order", "name"]


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["name"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "article_type",
        "category",
        "status",
        "published_at",
        "author",
    ]
    list_filter = ["status", "article_type", "category"]
    search_fields = ["title", "summary", "body"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["content_uuid", "created_at", "updated_at"]
    raw_id_fields = [
        "linked_topic",
        "linked_learning_unit",
        "linked_simulation",
        "author",
    ]
    filter_horizontal = ["tags", "related_articles"]
    actions = ["publish_articles", "archive_articles"]

    @admin.action(description="Publish selected articles")
    def publish_articles(self, request, queryset):
        now = timezone.now()
        updated_count = 0
        for article in queryset:
            article.status = "published"
            if not article.published_at:
                article.published_at = now
            article.save()
            updated_count += 1
        cache.delete_many(CACHE_KEYS_TO_INVALIDATE)
        if request:
            self.message_user(
                request, f"Successfully published {updated_count} article(s)."
            )

    @admin.action(description="Archive selected articles")
    def archive_articles(self, request, queryset):
        updated = queryset.update(status="archived")
        cache.delete_many(CACHE_KEYS_TO_INVALIDATE)
        if request:
            self.message_user(
                request, f"Successfully archived {updated} article(s)."
            )
