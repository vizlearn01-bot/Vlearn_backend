from django.urls import path
from knowledge.views import (
    ArticleListView,
    ArticleDetailView,
    CategoryDetailView,
    TagDetailView,
)

app_name = "knowledge"

urlpatterns = [
    path("", ArticleListView.as_view(), name="article-list"),
    path("category/<slug:slug>/", CategoryDetailView.as_view(), name="category-detail"),
    path("tag/<slug:slug>/", TagDetailView.as_view(), name="tag-detail"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article-detail"),
]
