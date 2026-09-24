from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from knowledge.models import Article, ArticleCategory, ArticleTag


CACHE_KEYS_TO_INVALIDATE = [
    "knowledge_all_categories",
    "knowledge_popular_tags",
]


@receiver([post_save, post_delete], sender=Article)
def invalidate_article_cache(sender, instance, **kwargs):
    """
    Invalidate popular tags and related taxonomy caches when an article is modified or removed.
    """
    cache.delete_many(CACHE_KEYS_TO_INVALIDATE)


@receiver([post_save, post_delete], sender=ArticleCategory)
def invalidate_category_cache(sender, instance, **kwargs):
    """
    Invalidate categories cache when a category is updated or deleted.
    """
    cache.delete("knowledge_all_categories")


@receiver([post_save, post_delete], sender=ArticleTag)
def invalidate_tag_cache(sender, instance, **kwargs):
    """
    Invalidate tags cache when a tag is updated or deleted.
    """
    cache.delete("knowledge_popular_tags")
