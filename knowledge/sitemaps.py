from urllib.parse import urlparse
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.db.models import Max, Q
from knowledge.models import Article, ArticleCategory, ArticleTag


class CustomSite:
    def __init__(self, domain: str, name: str = "VizLearn"):
        self.domain = domain
        self.name = name


class BaseVizLearnSitemap(Sitemap):
    protocol = "https"

    def get_urls(self, page=1, site=None, protocol=None):
        base_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org")
        parsed = urlparse(base_url)
        domain = parsed.netloc or "www.vizlearn.org"
        proto = parsed.scheme or "https"
        custom_site = CustomSite(domain=domain, name="VizLearn")
        return super().get_urls(page=page, site=custom_site, protocol=proto)


class KnowledgeIndexSitemap(BaseVizLearnSitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ["knowledge-index"]

    def location(self, item):
        return "/knowledge/"

    def lastmod(self, item):
        latest = (
            Article.objects.filter(status="published")
            .order_by("-updated_at")
            .first()
        )
        return latest.updated_at if latest else None


class StaticPageSitemap(BaseVizLearnSitemap):
    def items(self):
        return ["/", "/subscription", "/contact"]

    def location(self, item):
        return item

    def priority(self, item):
        return 0.8 if item == "/" else 0.6

    def changefreq(self, item):
        return "daily" if item == "/" else "weekly"


class KnowledgeArticleSitemap(BaseVizLearnSitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return (
            Article.objects.filter(status="published")
            .only("slug", "updated_at")
            .order_by("-updated_at")
        )

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f"/knowledge/{obj.slug}/"


class KnowledgeCategorySitemap(BaseVizLearnSitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        # Only index categories that have at least one published article
        return (
            ArticleCategory.objects.filter(articles__status="published")
            .annotate(
                latest_updated=Max(
                    "articles__updated_at",
                    filter=Q(articles__status="published"),
                )
            )
            .distinct()
            .only("slug", "order", "name", "created_at")
            .order_by("order", "name")
        )

    def location(self, obj):
        return f"/knowledge/category/{obj.slug}/"

    def lastmod(self, obj):
        return getattr(obj, "latest_updated", None) or obj.created_at


class KnowledgeTagSitemap(BaseVizLearnSitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        # Only index tags that have at least one published article
        return (
            ArticleTag.objects.filter(articles__status="published")
            .annotate(
                latest_updated=Max(
                    "articles__updated_at",
                    filter=Q(articles__status="published"),
                )
            )
            .distinct()
            .only("slug", "name", "created_at")
            .order_by("name")
        )

    def location(self, obj):
        return f"/knowledge/tag/{obj.slug}/"

    def lastmod(self, obj):
        return getattr(obj, "latest_updated", None) or obj.created_at


sitemaps = {
    "index": KnowledgeIndexSitemap,
    "static": StaticPageSitemap,
    "articles": KnowledgeArticleSitemap,
    "categories": KnowledgeCategorySitemap,
    "tags": KnowledgeTagSitemap,
}
