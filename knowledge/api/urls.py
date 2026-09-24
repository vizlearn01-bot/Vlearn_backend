from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AdminArticleViewSet,
    CurriculumLinkOptionsView,
    PublicArticleViewSet,
    PublicCategoryViewSet,
    PublicTagViewSet,
)

router = DefaultRouter()
router.register(r"articles", PublicArticleViewSet, basename="public-article")
router.register(r"categories", PublicCategoryViewSet, basename="category")
router.register(r"tags", PublicTagViewSet, basename="tag")
router.register(r"admin/articles", AdminArticleViewSet, basename="admin-article")

urlpatterns = [
    path(
        "curriculum-links/",
        CurriculumLinkOptionsView.as_view(),
        name="curriculum-links",
    ),
    path(
        "articles/<slug:slug>/publish/",
        AdminArticleViewSet.as_view({"post": "publish"}),
        name="article-publish",
    ),
    path(
        "articles/<slug:slug>/archive/",
        AdminArticleViewSet.as_view({"post": "archive"}),
        name="article-archive",
    ),
    path(
        "search/",
        PublicArticleViewSet.as_view({"get": "list"}),
        name="knowledge-search-api",
    ),
    path("", include(router.urls)),
]
