from django.db import models
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView

from Resources.permissions import IsPlatformAdmin
from curriculum.models import Concept, ConceptRelationship, LearningUnit, Simulation, Subject, Topic
from knowledge.models import Article, ArticleCategory, ArticleTag
from .serializers import (
    AdminArticleSerializer,
    ArticleCategorySerializer,
    ArticleTagSerializer,
    CurriculumLearningUnitOptionSerializer,
    CurriculumSimulationOptionSerializer,
    CurriculumTopicOptionSerializer,
    PublicArticleDetailSerializer,
    PublicArticleListSerializer,
)


class PublicArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only endpoint for browsing and reading published articles.
    Drafts and archived articles are strictly omitted from public views.
    """
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle]
    lookup_field = "slug"

    def get_queryset(self):
        status_param = self.request.query_params.get("status")
        target_status = "published"
        # Enforce permission check if client attempts to query unpublished status
        if status_param and status_param != "published":
            user = self.request.user
            is_admin = (
                user
                and user.is_authenticated
                and (
                    user.is_superuser
                    or getattr(user, "is_staff", False)
                    or getattr(user, "role", None) == "platform_admin"
                )
            )
            if not is_admin:
                raise PermissionDenied(
                    "You do not have permission to view unpublished articles."
                )
            target_status = status_param

        queryset = (
            Article.objects.filter(status=target_status)
            .select_related(
                "category",
                "author",
                "linked_topic",
                "linked_topic__subject",
                "linked_learning_unit",
                "linked_simulation",
            )
            .prefetch_related("tags", "related_articles")
            .order_by("-published_at", "-created_at")
        )

        if getattr(self, "action", None) == "retrieve":
            concept_prefetch = Prefetch(
                "concepts",
                queryset=Concept.objects.prefetch_related(
                    "misconceptions",
                    Prefetch(
                        "outgoing_relationships",
                        queryset=ConceptRelationship.objects.select_related("target"),
                    ),
                ),
            )
            queryset = queryset.prefetch_related(
                Prefetch(
                    "linked_learning_unit__concepts",
                    queryset=Concept.objects.prefetch_related(
                        "misconceptions",
                        Prefetch(
                            "outgoing_relationships",
                            queryset=ConceptRelationship.objects.select_related("target"),
                        ),
                    ),
                ),
                Prefetch(
                    "linked_topic__learning_units",
                    queryset=LearningUnit.objects.prefetch_related(concept_prefetch),
                ),
            )

        category_slug = self.request.query_params.get("category")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        tag_slug = self.request.query_params.get("tag")
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)

        article_type = self.request.query_params.get("article_type")
        if article_type:
            queryset = queryset.filter(article_type=article_type)

        search_query = self.request.query_params.get("search") or self.request.query_params.get("q")
        if search_query:
            from knowledge.search import search_articles
            queryset = search_articles(queryset, search_query)

        return queryset

    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request):
        """
        Dedicated search action: GET /api/knowledge/articles/search/?q=<query>
        """
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PublicArticleDetailSerializer
        return PublicArticleListSerializer


class PublicCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only endpoint for listing article categories.
    """
    permission_classes = [AllowAny]
    lookup_field = "slug"
    queryset = ArticleCategory.objects.all().order_by("order", "name")
    serializer_class = ArticleCategorySerializer


class PublicTagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only endpoint for listing article tags.
    """
    permission_classes = [AllowAny]
    lookup_field = "slug"
    queryset = ArticleTag.objects.all().order_by("name")
    serializer_class = ArticleTagSerializer


class AdminArticleViewSet(viewsets.ModelViewSet):
    """
    Platform admin endpoint for full article management (drafts, editing, publishing, archiving).
    """
    permission_classes = [IsPlatformAdmin]
    lookup_field = "slug"
    serializer_class = AdminArticleSerializer

    def get_queryset(self):
        queryset = (
            Article.objects.all()
            .select_related(
                "category",
                "author",
                "linked_topic",
                "linked_topic__subject",
                "linked_learning_unit",
                "linked_simulation",
            )
            .prefetch_related("tags", "related_articles")
            .order_by("-created_at")
        )

        status_param = self.request.query_params.get("status")
        if status_param:
            queryset = queryset.filter(status=status_param)

        category_param = self.request.query_params.get("category")
        if category_param:
            queryset = queryset.filter(category__slug=category_param)

        search_query = self.request.query_params.get("search") or self.request.query_params.get("q")
        if search_query:
            queryset = queryset.filter(
                models.Q(title__icontains=search_query)
                | models.Q(summary__icontains=search_query)
                | models.Q(body__icontains=search_query)
            )

        return queryset

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup_value = self.kwargs.get(lookup_url_kwarg)
        if lookup_value and str(lookup_value).isdigit():
            return get_object_or_404(
                self.filter_queryset(self.get_queryset()), pk=int(lookup_value)
            )
        return super().get_object()

    def perform_create(self, serializer):
        if "author" not in serializer.validated_data and self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            serializer.save()

    @action(detail=True, methods=["post"])
    def publish(self, request, slug=None):
        article = self.get_object()
        article.status = "published"
        if not article.published_at:
            article.published_at = timezone.now()
        article.save()
        serializer = self.get_serializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def archive(self, request, slug=None):
        article = self.get_object()
        article.status = "archived"
        article.save()
        serializer = self.get_serializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CurriculumLinkOptionsView(APIView):
    """
    Returns available subjects, topics, learning units, and simulations
    to populate dropdown selectors in the admin authoring UI.
    """
    permission_classes = [IsPlatformAdmin]

    def get(self, request, *args, **kwargs):
        subjects_qs = (
            Subject.objects.all()
            .values("id", "name")
            .order_by("name")
        )
        topics_qs = (
            Topic.objects.select_related("subject")
            .all()
            .order_by("subject__name", "order")
        )
        learning_units_qs = (
            LearningUnit.objects.select_related("topic")
            .all()
            .order_by("topic__name", "order")
        )
        simulations_qs = Simulation.objects.filter(status="ACTIVE").order_by("title")
        if not simulations_qs.exists():
            simulations_qs = Simulation.objects.all().order_by("title")

        return Response(
            {
                "subjects": list(subjects_qs),
                "topics": CurriculumTopicOptionSerializer(topics_qs, many=True).data,
                "learning_units": CurriculumLearningUnitOptionSerializer(
                    learning_units_qs, many=True
                ).data,
                "simulations": CurriculumSimulationOptionSerializer(
                    simulations_qs, many=True
                ).data,
            },
            status=status.HTTP_200_OK,
        )
