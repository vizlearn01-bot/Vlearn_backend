from django.db import connection, models
from knowledge.models import Article


def search_articles(queryset=None, query_string=None, category_slug=None, tag_slug=None):
    """
    Executes full-text search across published knowledge articles.
    
    If database vendor is PostgreSQL:
      Uses SearchVector ('title' A, 'summary' B, 'body' C), SearchQuery (websearch), and SearchRank.
      Ranks title matches highest, followed by summary, then body text.
    If SQLite or testing backend:
      Falls back cleanly to case-insensitive Q filters across title, summary, and body.
    """
    if queryset is None:
        queryset = Article.objects.filter(status="published")
    else:
        queryset = queryset.filter(status="published")

    if category_slug:
        queryset = queryset.filter(category__slug=category_slug)

    if tag_slug:
        queryset = queryset.filter(tags__slug=tag_slug)

    if not query_string or not query_string.strip():
        return queryset

    query_str = query_string.strip()

    if connection.vendor == "postgresql":
        from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

        vector = (
            SearchVector("title", weight="A")
            + SearchVector("summary", weight="B")
            + SearchVector("body", weight="C")
        )
        try:
            query = SearchQuery(query_str, search_type="websearch")
        except Exception:
            query = SearchQuery(query_str)

        return (
            queryset.annotate(search_rank=SearchRank(vector, query))
            .filter(
                models.Q(search_rank__gt=0.01)
                | models.Q(title__icontains=query_str)
                | models.Q(summary__icontains=query_str)
            )
            .order_by("-search_rank", "-published_at")
        )
    else:
        return (
            queryset.filter(
                models.Q(title__icontains=query_str)
                | models.Q(summary__icontains=query_str)
                | models.Q(body__icontains=query_str)
            )
            .order_by("-published_at")
        )
