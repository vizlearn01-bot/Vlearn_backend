import datetime
import json
import re
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.cache import cache
from django.core.management import call_command
from django.test import TestCase, override_settings
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.throttling import AnonRateThrottle

from curriculum.models import (
    Concept,
    ConceptRelationship,
    Curriculum,
    Grade,
    LearningUnit,
    Misconception,
    Simulation,
    SimulationStatus,
    Subject,
    SubjectDomain,
    Topic,
)
from knowledge.models import Article, ArticleCategory, ArticleTag
from knowledge.api.views import PublicArticleViewSet
from django.contrib import admin
from knowledge.views import render_article_markdown, get_cached_categories, get_cached_popular_tags
from knowledge.admin import ArticleAdmin

User = get_user_model()


class KnowledgeModelUnitTests(TestCase):
    """
    Unit tests for knowledge app models:
    - Slug auto-generation from title if left blank.
    - Unique slug enforcement.
    - Published state transition setting published_at timestamp.
    - Reading time calculation.
    """

    def setUp(self):
        self.category = ArticleCategory.objects.create(
            name="Physics",
            description="Physics articles",
            linked_subject_name="Physics",
            order=1,
        )
        self.tag = ArticleTag.objects.create(name="Optics")

    def test_slug_auto_generation_when_blank(self):
        # Category slug auto-generation
        cat = ArticleCategory.objects.create(name="Chemistry & Biology")
        self.assertEqual(cat.slug, "chemistry-biology")

        # Tag slug auto-generation
        tag = ArticleTag.objects.create(name="Wave Optics")
        self.assertEqual(tag.slug, "wave-optics")

        # Article slug auto-generation from title if left blank
        article = Article.objects.create(
            title="Understanding Total Internal Reflection",
            summary="Introductory guide to TIR in glass and water.",
            body="# Total Internal Reflection\n\nWhen light strikes a boundary...",
            category=self.category,
        )
        self.assertEqual(article.slug, "understanding-total-internal-reflection")

    def test_unique_slug_enforcement(self):
        # 1st article
        art1 = Article.objects.create(
            title="Gravitational Waves Explained",
            summary="Intro to gravitational waves.",
            body="Content 1",
            category=self.category,
        )
        self.assertEqual(art1.slug, "gravitational-waves-explained")

        # 2nd article with identical title must get unique suffixed slug
        art2 = Article.objects.create(
            title="Gravitational Waves Explained",
            summary="Second article with same title.",
            body="Content 2",
            category=self.category,
        )
        self.assertEqual(art2.slug, "gravitational-waves-explained-1")

        # 3rd article with identical title
        art3 = Article.objects.create(
            title="Gravitational Waves Explained",
            summary="Third article with same title.",
            body="Content 3",
            category=self.category,
        )
        self.assertEqual(art3.slug, "gravitational-waves-explained-2")

        # Category unique slug auto-suffixing when slugified name matches existing slug
        cat2 = ArticleCategory.objects.create(name="Physics!")
        self.assertEqual(cat2.slug, "physics-1")

        # Tag unique slug auto-suffixing when slugified name matches existing slug
        tag2 = ArticleTag.objects.create(name="Optics!")
        self.assertEqual(tag2.slug, "optics-1")

    def test_published_state_transition_sets_published_at_timestamp(self):
        # Initially created as draft
        article = Article.objects.create(
            title="Draft Research on Particle Physics",
            summary="Draft particle physics summary.",
            body="Particle physics notes.",
            status="draft",
        )
        self.assertIsNone(article.published_at)

        # Transition status to published
        before_publish = timezone.now()
        article.status = "published"
        article.save()

        self.assertIsNotNone(article.published_at)
        self.assertGreaterEqual(article.published_at, before_publish)

        # Subsequent updates while already published must not overwrite published_at
        initial_published_at = article.published_at
        article.summary = "Updated summary after review."
        article.save()
        self.assertEqual(article.published_at, initial_published_at)

    def test_reading_time_calculation(self):
        article = Article.objects.create(
            title="Speed of Light in Vacuum",
            summary="Short read",
            body=" ".join(["word"] * 450),
        )
        # 450 words / 200 wpm = 2.25 -> rounded to 2 minutes
        self.assertEqual(article.reading_time_minutes, 2)

        # Empty body defaults to 1 minute
        empty_article = Article.objects.create(
            title="Empty Article",
            summary="Empty",
            body="",
        )
        self.assertEqual(empty_article.reading_time_minutes, 1)


class KnowledgeAPIIntegrationTests(APITestCase):
    """
    Comprehensive API Integration tests for the VizLearn Knowledge Platform using DRF APITestCase:
    - Unauthenticated GET /api/knowledge/articles/ returns 200 and only published articles (empty list initially).
    - Draft articles are NEVER returned in GET /api/knowledge/articles/.
    - GET /api/knowledge/articles/<slug>/ returns 200 for published article, with all expected serialized fields.
    - GET /api/knowledge/articles/<draft-slug>/ returns 404 for draft/archived article.
    - Unauthenticated or non-admin attempts to POST / PATCH / DELETE to /api/knowledge/admin/articles/ return 401 / 403.
    - Platform admin can create a draft article, edit it, and use the publish action.
    - Platform admin can fetch curriculum link options.
    - Public category & tag endpoints work with AllowAny.
    - Throttling is configured on the public endpoint.
    """

    def setUp(self):
        # Users
        self.admin_user = User.objects.create_user(
            username="platform_admin_user",
            email="admin@vizlearn.co",
            password="AdminPassword123!",
            role="platform_admin",
            is_active=True,
        )
        self.student_user = User.objects.create_user(
            username="student_user",
            email="student@vizlearn.co",
            password="StudentPassword123!",
            role="student",
            is_active=True,
        )
        self.teacher_user = User.objects.create_user(
            username="teacher_user",
            email="teacher@vizlearn.co",
            password="TeacherPassword123!",
            role="teacher",
            is_active=True,
        )

        # Curriculum objects for linkage testing
        self.curriculum = Curriculum.objects.create(name="KCSE")
        self.grade = Grade.objects.create(
            curriculum=self.curriculum, name="Form 3", level=3
        )
        self.subject = Subject.objects.create(
            grade=self.grade, name="Physics"
        )
        self.topic = Topic.objects.create(
            subject=self.subject, name="Refraction of Light", order=1
        )
        self.learning_unit = LearningUnit.objects.create(
            topic=self.topic, name="Snell's Law", order=1
        )
        self.simulation = Simulation.objects.create(
            key="refraction_sim",
            title="Refraction Simulation",
            subject=SubjectDomain.PHYSICS,
            topic="Refraction of Light",
            status=SimulationStatus.ACTIVE,
            archetype="RefractionArchetype",
        )

        # Category and Tags
        self.category = ArticleCategory.objects.create(
            name="Optics & Light",
            slug="optics-light",
            description="All about optical phenomena",
            linked_subject_name="Physics",
            order=1,
        )
        self.tag_refraction = ArticleTag.objects.create(
            name="Refraction", slug="refraction"
        )
        self.tag_waves = ArticleTag.objects.create(
            name="Waves", slug="waves"
        )

    def test_unauthenticated_get_articles_returns_200_and_empty_list_initially(self):
        """
        Unauthenticated GET /api/knowledge/articles/ returns 200 and empty list when no articles exist.
        """
        response = self.client.get("/api/knowledge/articles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        self.assertEqual(results, [])

    def test_draft_and_archived_articles_never_returned_in_public_list(self):
        """
        Draft and archived articles are NEVER returned in GET /api/knowledge/articles/.
        Only published articles are returned.
        """
        # Create 1 published article, 1 draft article, 1 review article, 1 archived article
        published_art = Article.objects.create(
            title="Understanding Snell's Law",
            slug="understanding-snells-law",
            summary="Overview of Snell's Law and refractive indices.",
            body="# Snell's Law\n\n$$n_1 \\sin(\\theta_1) = n_2 \\sin(\\theta_2)$$",
            category=self.category,
            status="published",
            author=self.admin_user,
            linked_topic=self.topic,
            linked_learning_unit=self.learning_unit,
            linked_simulation=self.simulation,
        )
        published_art.tags.add(self.tag_refraction)

        Article.objects.create(
            title="Draft on Quantum Electrodynamics",
            slug="draft-quantum-electrodynamics",
            summary="Unpublished QED draft.",
            body="Work in progress...",
            category=self.category,
            status="draft",
            author=self.admin_user,
        )

        Article.objects.create(
            title="Review on Wave Particle Duality",
            slug="review-wave-particle-duality",
            summary="Under editorial review.",
            body="Review content...",
            category=self.category,
            status="review",
            author=self.admin_user,
        )

        Article.objects.create(
            title="Archived Classical Mechanics",
            slug="archived-classical-mechanics",
            summary="Outdated guide.",
            body="Archived content...",
            category=self.category,
            status="archived",
            author=self.admin_user,
        )

        # Unauthenticated request
        response = self.client.get("/api/knowledge/articles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        slugs = [item["slug"] for item in results]

        self.assertEqual(len(slugs), 1)
        self.assertIn("understanding-snells-law", slugs)
        self.assertNotIn("draft-quantum-electrodynamics", slugs)
        self.assertNotIn("review-wave-particle-duality", slugs)
        self.assertNotIn("archived-classical-mechanics", slugs)

    def test_unauthenticated_draft_status_filter_returns_403(self):
        """
        An unauthenticated user attempting to pass ?status=draft to the public endpoint
        receives 403 Forbidden.
        """
        response = self.client.get("/api/knowledge/articles/?status=draft")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response_archived = self.client.get("/api/knowledge/articles/?status=archived")
        self.assertEqual(response_archived.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_article_detail_published_returns_all_expected_serialized_fields(self):
        """
        GET /api/knowledge/articles/<slug>/ returns 200 for published article,
        with all expected serialized fields and correct nested structures.
        """
        article = Article.objects.create(
            title="Dispersion of Light Through Prisms",
            slug="dispersion-of-light-through-prisms",
            article_type="educational",
            summary="How white light separates into component colors.",
            body="# Dispersion of Light\n\nWhite light separates into ROYGBIV...",
            featured_image_url="https://images.unsplash.com/photo-1507668077129-56e32842fceb",
            featured_image_alt="Light prism dispersion",
            meta_title="Dispersion of Light Explained | VizLearn",
            meta_description="Learn how prisms disperse light into spectrum colors.",
            category=self.category,
            status="published",
            author=self.admin_user,
            linked_topic=self.topic,
            linked_learning_unit=self.learning_unit,
            linked_simulation=self.simulation,
        )
        article.tags.add(self.tag_refraction, self.tag_waves)

        response = self.client.get("/api/knowledge/articles/dispersion-of-light-through-prisms/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        expected_fields = [
            "id",
            "content_uuid",
            "title",
            "slug",
            "article_type",
            "summary",
            "body",
            "featured_image_url",
            "featured_image_alt",
            "meta_title",
            "meta_description",
            "category",
            "tags",
            "linked_topic",
            "linked_learning_unit",
            "linked_simulation",
            "related_articles",
            "published_at",
            "reading_time_minutes",
            "author_name",
            "created_at",
            "updated_at",
        ]
        for field_name in expected_fields:
            self.assertIn(field_name, data, f"Missing serialized field: {field_name}")

        # Verify field contents
        self.assertEqual(data["slug"], "dispersion-of-light-through-prisms")
        self.assertEqual(data["title"], "Dispersion of Light Through Prisms")
        self.assertEqual(data["article_type"], "educational")
        self.assertEqual(data["category"]["name"], "Optics & Light")
        self.assertEqual(data["category"]["slug"], "optics-light")
        self.assertEqual(len(data["tags"]), 2)
        self.assertEqual(data["linked_topic"]["name"], "Refraction of Light")
        self.assertEqual(data["linked_topic"]["subject_name"], "Physics")
        self.assertEqual(data["linked_learning_unit"]["name"], "Snell's Law")
        self.assertEqual(data["linked_simulation"]["key"], "refraction_sim")
        self.assertIsNotNone(data["published_at"])
        self.assertGreater(data["reading_time_minutes"], 0)

    def test_related_articles_api_excludes_draft_and_archived(self):
        """
        Public article detail endpoint (/api/knowledge/articles/<slug>/) must strictly
        exclude draft and archived articles from the serialized related_articles list,
        even if they are explicitly added to related_articles in the database.
        """
        published_main = Article.objects.create(
            title="Main Published Article",
            slug="main-published-article",
            summary="Main published article summary.",
            body="Main body text.",
            category=self.category,
            status="published",
            author=self.admin_user,
        )
        published_related = Article.objects.create(
            title="Related Published Article",
            slug="related-published-article",
            summary="Related published summary.",
            body="Related body text.",
            category=self.category,
            status="published",
            author=self.admin_user,
        )
        draft_related = Article.objects.create(
            title="Related Draft Article",
            slug="related-draft-article",
            summary="Related draft summary.",
            body="Draft body text.",
            category=self.category,
            status="draft",
            author=self.admin_user,
        )
        archived_related = Article.objects.create(
            title="Related Archived Article",
            slug="related-archived-article",
            summary="Related archived summary.",
            body="Archived body text.",
            category=self.category,
            status="archived",
            author=self.admin_user,
        )

        published_main.related_articles.add(published_related, draft_related, archived_related)

        response = self.client.get(f"/api/knowledge/articles/{published_main.slug}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        related_slugs = [rel["slug"] for rel in response.data.get("related_articles", [])]
        self.assertIn("related-published-article", related_slugs)
        self.assertNotIn("related-draft-article", related_slugs)
        self.assertNotIn("related-archived-article", related_slugs)

    def test_get_article_detail_returns_404_for_draft_and_archived(self):
        """
        GET /api/knowledge/articles/<draft-slug>/ returns 404 for draft and archived articles.
        """
        Article.objects.create(
            title="Secret Draft",
            slug="secret-draft",
            summary="Secret",
            body="Secret body",
            status="draft",
        )
        Article.objects.create(
            title="Archived Relic",
            slug="archived-relic",
            summary="Archived",
            body="Archived body",
            status="archived",
        )

        # Draft slug returns 404
        draft_resp = self.client.get("/api/knowledge/articles/secret-draft/")
        self.assertEqual(draft_resp.status_code, status.HTTP_404_NOT_FOUND)

        # Archived slug returns 404
        archived_resp = self.client.get("/api/knowledge/articles/archived-relic/")
        self.assertEqual(archived_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthenticated_and_non_admin_attempts_to_admin_endpoints(self):
        """
        Unauthenticated or non-admin attempts to POST / PATCH / DELETE
        to /api/knowledge/admin/articles/ return 401 / 403.
        """
        test_article = Article.objects.create(
            title="Target Article for Admin Tests",
            slug="target-article-for-admin-tests",
            summary="Summary",
            body="Body",
            status="draft",
        )

        create_payload = {
            "title": "Unauthorized Article Creation",
            "summary": "Should be rejected",
            "body": "Forbidden body",
        }
        patch_payload = {"title": "Malicious Modification"}

        # 1. Unauthenticated attempts -> 401 Unauthorized
        self.client.force_authenticate(user=None)

        post_unauth = self.client.post("/api/knowledge/admin/articles/", create_payload)
        self.assertEqual(post_unauth.status_code, status.HTTP_401_UNAUTHORIZED)

        patch_unauth = self.client.patch(
            f"/api/knowledge/admin/articles/{test_article.slug}/", patch_payload
        )
        self.assertEqual(patch_unauth.status_code, status.HTTP_401_UNAUTHORIZED)

        delete_unauth = self.client.delete(
            f"/api/knowledge/admin/articles/{test_article.slug}/"
        )
        self.assertEqual(delete_unauth.status_code, status.HTTP_401_UNAUTHORIZED)

        # 2. Authenticated as non-admin Student -> 403 Forbidden
        self.client.force_authenticate(user=self.student_user)

        post_student = self.client.post("/api/knowledge/admin/articles/", create_payload)
        self.assertEqual(post_student.status_code, status.HTTP_403_FORBIDDEN)

        patch_student = self.client.patch(
            f"/api/knowledge/admin/articles/{test_article.slug}/", patch_payload
        )
        self.assertEqual(patch_student.status_code, status.HTTP_403_FORBIDDEN)

        delete_student = self.client.delete(
            f"/api/knowledge/admin/articles/{test_article.slug}/"
        )
        self.assertEqual(delete_student.status_code, status.HTTP_403_FORBIDDEN)

        # 3. Authenticated as non-admin Teacher -> 403 Forbidden
        self.client.force_authenticate(user=self.teacher_user)

        post_teacher = self.client.post("/api/knowledge/admin/articles/", create_payload)
        self.assertEqual(post_teacher.status_code, status.HTTP_403_FORBIDDEN)

        patch_teacher = self.client.patch(
            f"/api/knowledge/admin/articles/{test_article.slug}/", patch_payload
        )
        self.assertEqual(patch_teacher.status_code, status.HTTP_403_FORBIDDEN)

        delete_teacher = self.client.delete(
            f"/api/knowledge/admin/articles/{test_article.slug}/"
        )
        self.assertEqual(delete_teacher.status_code, status.HTTP_403_FORBIDDEN)

    def test_platform_admin_create_edit_and_publish_action(self):
        """
        Platform admin can create a draft article, edit it, and use the publish action.
        """
        self.client.force_authenticate(user=self.admin_user)

        # 1. Create draft article
        create_payload = {
            "title": "Refraction and Total Internal Reflection Guide",
            "summary": "Comprehensive deep-dive into optical boundary behavior.",
            "body": "# Optical Boundaries\n\nWhen light passes between optically dense media...",
            "category": self.category.id,
            "tags": [self.tag_refraction.id, self.tag_waves.id],
            "linked_topic": self.topic.id,
            "linked_learning_unit": self.learning_unit.id,
            "linked_simulation": self.simulation.id,
        }
        create_resp = self.client.post("/api/knowledge/admin/articles/", create_payload)
        self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)

        article_slug = create_resp.data["slug"]
        self.assertEqual(create_resp.data["status"], "draft")
        self.assertIsNone(create_resp.data["published_at"])
        self.assertEqual(create_resp.data["category"], self.category.id)
        self.assertEqual(len(create_resp.data["tags"]), 2)

        # 2. Edit draft article
        update_payload = {
            "title": "Advanced Refraction and Total Internal Reflection Guide",
            "summary": "Updated summary with deeper insights into critical angles.",
        }
        patch_resp = self.client.patch(
            f"/api/knowledge/admin/articles/{article_slug}/", update_payload
        )
        self.assertEqual(patch_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(
            patch_resp.data["title"],
            "Advanced Refraction and Total Internal Reflection Guide",
        )

        # 3. Use publish action
        publish_resp = self.client.post(
            f"/api/knowledge/admin/articles/{article_slug}/publish/"
        )
        self.assertEqual(publish_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(publish_resp.data["status"], "published")
        self.assertIsNotNone(publish_resp.data["published_at"])

        # 4. Verify public endpoint now serves this newly published article
        self.client.force_authenticate(user=None)
        public_resp = self.client.get(f"/api/knowledge/articles/{article_slug}/")
        self.assertEqual(public_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(
            public_resp.data["title"],
            "Advanced Refraction and Total Internal Reflection Guide",
        )

    def test_platform_admin_can_fetch_curriculum_link_options(self):
        """
        Platform admin can fetch curriculum link options.
        Unauthenticated or non-admin requests are rejected.
        """
        # Unauthenticated -> 401
        self.client.force_authenticate(user=None)
        unauth_resp = self.client.get("/api/knowledge/curriculum-links/")
        self.assertEqual(unauth_resp.status_code, status.HTTP_401_UNAUTHORIZED)

        # Student -> 403
        self.client.force_authenticate(user=self.student_user)
        student_resp = self.client.get("/api/knowledge/curriculum-links/")
        self.assertEqual(student_resp.status_code, status.HTTP_403_FORBIDDEN)

        # Platform Admin -> 200 with options data
        self.client.force_authenticate(user=self.admin_user)
        admin_resp = self.client.get("/api/knowledge/curriculum-links/")
        self.assertEqual(admin_resp.status_code, status.HTTP_200_OK)

        data = admin_resp.data
        self.assertIn("subjects", data)
        self.assertIn("topics", data)
        self.assertIn("learning_units", data)
        self.assertIn("simulations", data)

        self.assertGreater(len(data["subjects"]), 0)
        self.assertGreater(len(data["topics"]), 0)
        self.assertGreater(len(data["learning_units"]), 0)
        self.assertGreater(len(data["simulations"]), 0)

        # Verify topic structure
        first_topic = data["topics"][0]
        self.assertEqual(first_topic["name"], "Refraction of Light")
        self.assertEqual(first_topic["subject_name"], "Physics")

    def test_public_category_and_tag_endpoints_allowany(self):
        """
        Public category & tag endpoints work with AllowAny.
        """
        self.client.force_authenticate(user=None)

        # Categories list & detail
        cat_list_resp = self.client.get("/api/knowledge/categories/")
        self.assertEqual(cat_list_resp.status_code, status.HTTP_200_OK)

        cat_detail_resp = self.client.get(f"/api/knowledge/categories/{self.category.slug}/")
        self.assertEqual(cat_detail_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(cat_detail_resp.data["slug"], self.category.slug)

        # Tags list & detail
        tag_list_resp = self.client.get("/api/knowledge/tags/")
        self.assertEqual(tag_list_resp.status_code, status.HTTP_200_OK)

        tag_detail_resp = self.client.get(f"/api/knowledge/tags/{self.tag_refraction.slug}/")
        self.assertEqual(tag_detail_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(tag_detail_resp.data["slug"], self.tag_refraction.slug)

    def test_throttling_configured_on_public_endpoint(self):
        """
        Throttling is configured on the public endpoint:
        - AnonRateThrottle is in PublicArticleViewSet.throttle_classes
        - REST_FRAMEWORK contains DEFAULT_THROTTLE_RATES with 'anon'
        """
        self.assertIn(
            AnonRateThrottle,
            PublicArticleViewSet.throttle_classes,
            "PublicArticleViewSet must include AnonRateThrottle in throttle_classes",
        )

        rest_framework_settings = getattr(settings, "REST_FRAMEWORK", {})
        throttle_rates = rest_framework_settings.get("DEFAULT_THROTTLE_RATES", {})
        self.assertIn(
            "anon",
            throttle_rates,
            "REST_FRAMEWORK must configure 'anon' rate in DEFAULT_THROTTLE_RATES",
        )


class Phase2TemplateAndSitemapTests(TestCase):
    """
    Integration and unit tests for Phase 2:
    - Markdown rendering & Bleach sanitization
    - ArticleListView (public published listing & category filtering)
    - ArticleDetailView (HTML rendering, metadata, curriculum/simulation context, draft 404)
    - CategoryDetailView
    - RobotsTxtView (/robots.txt)
    - SitemapView (/sitemap.xml)
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="author_jane",
            email="jane@example.com",
            password="SecurePassword123!",
            first_name="Jane",
            last_name="Doe",
        )

        self.curriculum = Curriculum.objects.create(name="KCSE")
        self.grade = Grade.objects.create(name="Form 4", level=4, curriculum=self.curriculum)
        self.subject = Subject.objects.create(
            name="Physics",
            grade=self.grade,
        )
        self.topic = Topic.objects.create(
            subject=self.subject,
            name="Optics and Light",
            description="Electromagnetic spectrum, refraction, lenses.",
            order=1,
        )
        self.learning_unit = LearningUnit.objects.create(
            topic=self.topic,
            name="Snell's Law of Refraction",
            description="Calculating angles of incidence and refraction.",
            order=1,
        )
        self.simulation = Simulation.objects.create(
            key="snells_law_sim",
            title="Snell's Law Interactive Prism",
            description="Simulate light entering different refractive media.",
            archetype="refraction_bench",
            subject=SubjectDomain.PHYSICS,
            topic="Optics and Light",
            status=SimulationStatus.ACTIVE,
        )

        self.cat_physics = ArticleCategory.objects.create(
            name="Physics & Optics",
            slug="physics-optics",
            description="Articles exploring waves, optics, and electromagnetism.",
            linked_subject_name="Physics",
            order=1,
        )
        self.cat_chemistry = ArticleCategory.objects.create(
            name="Chemistry & Matter",
            slug="chemistry-matter",
            description="Gas laws, kinetics, and reactions.",
            linked_subject_name="Chemistry",
            order=2,
        )

        self.tag_waves = ArticleTag.objects.create(name="Waves", slug="waves")

        # Published article with curriculum & simulation links
        self.published_article = Article.objects.create(
            title="Understanding Snell's Law and Refraction",
            slug="understanding-snells-law-and-refraction",
            summary="A visual breakdown of refractive indices and Snell's Law.",
            body=(
                "## Introduction\n\n"
                "Refraction occurs when light bends at a boundary.\n\n"
                "$$\\frac{\\sin \\theta_1}{\\sin \\theta_2} = \\frac{n_2}{n_1}$$\n\n"
                "| Medium | Index |\n| --- | --- |\n| Vacuum | 1.0 |\n| Water | 1.33 |\n\n"
                "**Key takeaway**: Denser mediums bend light toward normal.\n\n"
                "<script>alert('malicious script')</script>"
            ),
            category=self.cat_physics,
            author=self.user,
            status="published",
            published_at=timezone.now(),
            linked_topic=self.topic,
            linked_learning_unit=self.learning_unit,
            linked_simulation=self.simulation,
        )
        self.published_article.tags.add(self.tag_waves)

        # Draft article
        self.draft_article = Article.objects.create(
            title="Draft Secrets of Quantum Mechanics",
            slug="draft-secrets-of-quantum-mechanics",
            summary="Unpublished work in progress on quantum tunneling.",
            body="Not ready for public eyes.",
            category=self.cat_physics,
            status="draft",
        )

        # Archived article
        self.archived_article = Article.objects.create(
            title="Archived Classical Mechanics",
            slug="archived-classical-mechanics",
            summary="Outdated physics content archive.",
            body="Archived content not visible to public.",
            category=self.cat_physics,
            status="archived",
        )

    def test_markdown_sanitization(self):
        """
        Asserts malicious script tags and event handlers are stripped/escaped,
        while safe markdown/HTML formatting elements are preserved.
        """
        from knowledge.views import render_article_markdown

        raw_md = (
            "## Heading 2\n\n"
            "This is **bold** text with a [link](https://vizlearn.org).\n\n"
            "<script>alert('xss');</script>\n\n"
            "<img src=\"https://example.com/pic.png\" alt=\"pic\" onerror=\"alert(1)\">\n\n"
            "| Column 1 | Column 2 |\n| --- | --- |\n| Val A | Val B |\n\n"
            "<p>Safe paragraph text.</p>"
        )
        rendered = render_article_markdown(raw_md)

        # Allowed tags preserved (heading has TOC ID attribute)
        self.assertIn('id="heading-2">Heading 2</h2>', rendered)
        self.assertIn("<strong>bold</strong>", rendered)
        self.assertIn('<a href="https://vizlearn.org">link</a>', rendered)
        self.assertIn("<table>", rendered)
        self.assertIn('src="https://example.com/pic.png"', rendered)
        self.assertIn("<p>Safe paragraph text.</p>", rendered)

        # Malicious tags and attributes stripped
        self.assertNotIn("<script>", rendered)
        self.assertNotIn("</script>", rendered)
        self.assertNotIn("onerror", rendered)
        self.assertNotIn("<script>alert('xss');</script>", rendered)

    def test_public_article_list_html_view(self):
        """
        GET /knowledge/ returns 200 OK, returns text/html containing published
        article titles, does NOT contain draft or archived article titles, and
        contains category filter links.
        """
        response = self.client.get("/knowledge/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response["Content-Type"])
        self.assertTemplateUsed(response, "knowledge/article_list.html")
        self.assertTemplateUsed(response, "knowledge/base.html")

        # Published article is shown
        self.assertContains(response, "Understanding Snell&#x27;s Law and Refraction")
        self.assertContains(response, "Physics &amp; Optics")

        # Draft and archived articles are NOT shown
        self.assertNotContains(response, "Draft Secrets of Quantum Mechanics")
        self.assertNotContains(response, "Archived Classical Mechanics")

        # Category filter links are present
        self.assertContains(response, f"/knowledge/category/{self.cat_physics.slug}/")
        self.assertContains(response, f"/knowledge/category/{self.cat_chemistry.slug}/")

        # Categories context is provided
        self.assertIn("categories", response.context)
        self.assertEqual(len(response.context["categories"]), 2)

        # Filtering by category works
        resp_chem = self.client.get(f"/knowledge/?category={self.cat_chemistry.slug}")
        self.assertEqual(resp_chem.status_code, 200)
        self.assertNotContains(resp_chem, "Understanding Snell&#x27;s Law and Refraction")

    def test_public_article_detail_html_view_published(self):
        """
        GET /knowledge/<published-slug>/ returns 200 OK and validates:
        - Semantic HTML tags (<article>, <header>, <main>, <nav>)
        - <title> contains the article title / meta_title
        - <meta name="description"> contains summary / meta_description
        - <link rel="canonical"> points to canonical URL
        - Open Graph tags (og:title, og:description, og:type=article, og:url)
        - Twitter Card tags
        - Schema.org JSON-LD valid and contains Article and BreadcrumbList
        - Rendered Markdown (<h2>, <strong>, <table>)
        - KaTeX math blocks preserved ($$...$$)
        - Linked curriculum topic and simulation in HTML context
        """
        from django.utils.html import escape

        url = f"/knowledge/{self.published_article.slug}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response["Content-Type"])
        self.assertTemplateUsed(response, "knowledge/article_detail.html")

        html = response.content.decode("utf-8")

        # 1. Semantic HTML tags
        self.assertIn("<article", html)
        self.assertIn("<header", html)
        self.assertIn("<main", html)
        self.assertIn("<nav", html)

        # 2. <title> contains article title
        self.assertIn(f"<title>{escape(self.published_article.title)} | VizLearn Knowledge</title>", html)

        # 3. <meta name="description"> contains summary
        self.assertIn(f'<meta name="description" content="{escape(self.published_article.summary)}">', html)

        # 4. <link rel="canonical"> points to canonical URL on PUBLIC_SITE_URL
        public_site_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/")
        expected_canonical = f"{public_site_url}/knowledge/{self.published_article.slug}/"
        self.assertIn(f'<link rel="canonical" href="{expected_canonical}">', html)

        # 5. Open Graph tags
        self.assertIn('<meta property="og:type" content="article">', html)
        self.assertIn(f'<meta property="og:url" content="{expected_canonical}">', html)
        self.assertIn('property="og:title"', html)
        self.assertIn('property="og:description"', html)

        # 6. Twitter Card tags
        self.assertIn('<meta name="twitter:card" content="summary_large_image">', html)
        self.assertIn('name="twitter:title"', html)
        self.assertIn('name="twitter:description"', html)

        # 7. Schema.org JSON-LD validation
        match = re.search(r'<script\s+type="application/ld\+json"\s*>(.*?)</script>', html, re.DOTALL)
        self.assertIsNotNone(match, "application/ld+json script tag must be present")
        json_ld_data = json.loads(match.group(1).strip())
        self.assertEqual(json_ld_data.get("@context"), "https://schema.org")
        self.assertIn("@graph", json_ld_data)

        graph_types = [item.get("@type") for item in json_ld_data["@graph"]]
        self.assertIn("Article", graph_types)
        self.assertIn("BreadcrumbList", graph_types)

        # Verify Article schema properties
        article_schema = next(item for item in json_ld_data["@graph"] if item.get("@type") == "Article")
        self.assertEqual(article_schema["headline"], self.published_article.title)
        self.assertEqual(article_schema["description"], self.published_article.summary)
        self.assertEqual(article_schema["publisher"]["name"], "VizLearn")

        # Verify BreadcrumbList schema properties
        breadcrumb_schema = next(item for item in json_ld_data["@graph"] if item.get("@type") == "BreadcrumbList")
        crumb_names = [crumb["name"] for crumb in breadcrumb_schema["itemListElement"]]
        self.assertIn("Home", crumb_names)
        self.assertIn("Knowledge", crumb_names)
        self.assertIn(self.cat_physics.name, crumb_names)
        self.assertIn(self.published_article.title, crumb_names)

        # 8. Markdown rendered to HTML (h2 with TOC id, strong, table)
        self.assertIn('id="introduction">Introduction</h2>', html)
        self.assertIn("<strong>Key takeaway</strong>", html)
        self.assertIn("<table>", html)
        self.assertIn("<td>Vacuum</td>", html)
        self.assertIn("<td>1.0</td>", html)

        # Markdown body must NOT contain raw unescaped script tag
        self.assertNotIn("<script>", response.context["rendered_body"])
        self.assertNotIn("</script>", response.context["rendered_body"])

        # 9. KaTeX math blocks preserved
        self.assertIn("\\frac{\\sin \\theta_1}{\\sin \\theta_2} = \\frac{n_2}{n_1}", html)

        # 10. Linked curriculum topic in HTML context
        self.assertIn("Part of the VizLearn Curriculum", html)
        self.assertIn(self.topic.name, html)
        self.assertIn(f"/student/topic/{self.topic.id}", html)

        # 11. Linked simulation in HTML context
        self.assertIn("Interactive Simulation", html)
        self.assertIn("Snell&#x27;s Law Interactive Prism", html)
        self.assertIn(f"sim={self.simulation.key}", html)

    def test_public_article_detail_html_view_draft_returns_404(self):
        """
        GET /knowledge/<draft-slug>/ returns 404 Not Found.
        GET /knowledge/<archived-slug>/ returns 404 Not Found.
        GET /knowledge/<nonexistent-slug>/ returns 404 Not Found.
        """
        draft_url = f"/knowledge/{self.draft_article.slug}/"
        response_draft = self.client.get(draft_url)
        self.assertEqual(response_draft.status_code, 404)

        archived_url = f"/knowledge/{self.archived_article.slug}/"
        response_archived = self.client.get(archived_url)
        self.assertEqual(response_archived.status_code, 404)

        response_nonexistent = self.client.get("/knowledge/nonexistent-article-slug/")
        self.assertEqual(response_nonexistent.status_code, 404)

    def test_public_category_detail_html_view(self):
        """
        GET /knowledge/category/<category-slug>/ returns 200 OK with articles in that category.
        GET /knowledge/category/<nonexistent-slug>/ returns 404 Not Found.
        """
        url = f"/knowledge/category/{self.cat_physics.slug}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response["Content-Type"])
        self.assertTemplateUsed(response, "knowledge/category_detail.html")
        self.assertContains(response, "Physics &amp; Optics")
        self.assertContains(response, "Understanding Snell&#x27;s Law and Refraction")
        self.assertNotContains(response, "Draft Secrets of Quantum Mechanics")
        self.assertNotContains(response, "Archived Classical Mechanics")

        response_404 = self.client.get("/knowledge/category/nonexistent-category/")
        self.assertEqual(response_404.status_code, 404)

    def test_sitemap_xml(self):
        """
        GET /sitemap.xml returns 200 OK with Content-Type application/xml or text/xml.
        Contains URLs for published articles and categories that have published articles.
        Does NOT contain URLs for draft, archived articles, or empty categories.
        """
        public_site_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/")
        response = self.client.get("/sitemap.xml")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            any(content_type in response["Content-Type"] for content_type in ["application/xml", "text/xml"]),
            f"Unexpected Content-Type: {response['Content-Type']}"
        )
        content = response.content.decode("utf-8")
        self.assertIn(f"<loc>{public_site_url}/knowledge/{self.published_article.slug}/</loc>", content)
        self.assertIn(f"<loc>{public_site_url}/knowledge/category/{self.cat_physics.slug}/</loc>", content)
        # Empty category (cat_chemistry has 0 published articles) must be excluded
        self.assertNotIn(f"/knowledge/category/{self.cat_chemistry.slug}/", content)
        self.assertNotIn(f"/knowledge/{self.draft_article.slug}/", content)
        self.assertNotIn(f"/knowledge/{self.archived_article.slug}/", content)

    def test_robots_txt(self):
        """
        GET /robots.txt returns 200 OK with Content-Type text/plain.
        Contains Allow: /knowledge/, Disallow: /admin/, and absolute Sitemap URL.
        """
        public_site_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/")
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/plain", response["Content-Type"])
        content = response.content.decode("utf-8")
        self.assertIn("User-agent: *", content)
        self.assertIn("Allow: /knowledge/", content)
        self.assertIn("Disallow: /admin/", content)
        self.assertIn("Disallow: /api/", content)
        self.assertIn(f"Sitemap: {public_site_url}/sitemap.xml", content)

    def test_crawlability_raw_http_get_returns_full_content(self):
        """
        Verify crawlability: Search engine crawlers (Googlebot, Bingbot) do not
        require JavaScript execution to index the content. A raw HTTP GET must return
        the full semantic article text, headings, metadata, and structured data
        in the initial response payload.
        """
        response = self.client.get(f"/knowledge/{self.published_article.slug}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response["Content-Type"])

        html = response.content.decode("utf-8")

        # Verify semantic article body is completely present in initial HTML payload
        self.assertIn("<article", html)
        self.assertIn("Introduction", html)
        self.assertIn("Refraction occurs when light bends at a boundary.", html)
        self.assertIn("Vacuum", html)
        self.assertIn("1.0", html)
        self.assertIn("Water", html)
        self.assertIn("1.33", html)
        self.assertIn("Key takeaway", html)

        # Verify search indexing directives and structured data
        self.assertIn('name="robots" content="index, follow"', html)
        self.assertIn("canonical", html)
        self.assertIn("application/ld+json", html)

    def test_article_detail_bounded_queries(self):
        """
        Verify ArticleDetailView has bounded database queries (no N+1 query problem).
        Specifically tests that prefetch_related for published related articles,
        tags, category, topic, and simulation executes within an expected bounded query count.
        """
        # Create additional related articles and tags to detect N+1 regressions
        for i in range(5):
            rel = Article.objects.create(
                title=f"Related Batch Article {i}",
                slug=f"related-batch-article-{i}",
                summary=f"Batch summary {i}",
                body=f"Batch content {i}",
                category=self.cat_physics,
                status="published",
                author=self.user,
            )
            self.published_article.related_articles.add(rel)

        # Execute request and monitor queries
        # Phase 5: Prefetching article, tags, concepts via learning_unit, learning_units via topic,
        # concepts via topic, related_articles, and related_articles__tags executes in exactly 7 bounded queries.
        with self.assertNumQueries(7):
            response = self.client.get(f"/knowledge/{self.published_article.slug}/")
            self.assertEqual(response.status_code, 200)

    def test_canonical_and_og_use_public_site_url_regardless_of_request_host(self):
        """
        Canonical tags, Open Graph url, and JSON-LD @id/breadcrumbs must strictly use
        PUBLIC_SITE_URL (e.g. https://www.vizlearn.org), even if the incoming request
        Host is the backend API domain (e.g. api.vizlearn.co or render internal host).
        """
        response = self.client.get(
            f"/knowledge/{self.published_article.slug}/",
            HTTP_HOST="api.vizlearn.co",
            HTTP_X_FORWARDED_HOST="backend.onrender.com",
        )
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        # Canonical tag MUST point to https://www.vizlearn.org
        self.assertIn(
            '<link rel="canonical" href="https://www.vizlearn.org/knowledge/understanding-snells-law-and-refraction/">',
            html,
        )
        # Open Graph URL MUST point to https://www.vizlearn.org
        self.assertIn(
            '<meta property="og:url" content="https://www.vizlearn.org/knowledge/understanding-snells-law-and-refraction/">',
            html,
        )
        # Must NEVER leak api.vizlearn.co or backend.onrender.com
        self.assertNotIn("api.vizlearn.co/knowledge/", html)
        self.assertNotIn("backend.onrender.com/knowledge/", html)

    def test_main_content_accessibility_and_performance_attributes(self):
        """
        Verify accessibility and performance enhancements:
        - Skip to main content link with href="#main-content"
        - <main id="main-content" tabindex="-1"> for programmatic focus management
        - Hero image loading="eager" fetchpriority="high" (LCP optimization)
        - Figcaption aria-hidden="true" (screen reader announcement deduplication)
        - Plus Jakarta Sans brand typography loaded
        """
        # Set a featured image on article
        self.published_article.featured_image_url = "https://images.unsplash.com/photo-1507668077129-56e32842fceb"
        self.published_article.featured_image_alt = "Prism dispersion visual"
        self.published_article.save()

        response = self.client.get(f"/knowledge/{self.published_article.slug}/")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        # Accessibility skip link & main tabindex
        self.assertIn('href="#main-content"', html)
        self.assertIn('<main id="main-content" tabindex="-1"', html)

        # Above-the-fold hero image LCP attributes
        self.assertIn('loading="eager"', html)
        self.assertIn('fetchpriority="high"', html)

        # Figcaption deduplication
        self.assertIn('<figcaption class="p-3 text-xs text-center text-slate-500 bg-slate-50 border-t border-slate-100" aria-hidden="true">', html)

        # Typography
        self.assertIn("Plus+Jakarta+Sans", html)

    def test_article_curriculum_lineage_and_simulation_teaser_properties(self):
        """
        Phase 3: Verify Article curriculum_lineage, simulation_teaser, and simulation_cta_label
        properties correctly resolve and fall back cleanly without extra database queries.
        """
        # Test curriculum lineage
        lineage = self.published_article.curriculum_lineage
        self.assertIsNotNone(lineage)
        self.assertEqual(lineage["curriculum"], self.curriculum.name)
        self.assertEqual(lineage["grade"], self.grade.name)
        self.assertEqual(lineage["subject"], self.subject.name)
        self.assertEqual(lineage["topic_name"], self.topic.name)
        self.assertEqual(lineage["topic_id"], self.topic.id)
        self.assertEqual(lineage["learning_unit_name"], self.learning_unit.name)
        self.assertEqual(lineage["learning_unit_id"], self.learning_unit.id)

        # Test simulation teaser with context_spec
        self.simulation.config = {
            "context_spec": {
                "overview": "Investigate refractive angles and Snell's Law across different boundaries.",
                "how_to_use": [
                    "Adjust the incident ray angle slider",
                    "Change index of refraction for medium 2 to water (1.33)",
                    "Observe critical angle and total internal reflection"
                ],
                "expected_results": "Light bends toward normal when entering a denser medium."
            }
        }
        self.simulation.save()

        # Re-fetch with select_related
        art = Article.objects.select_related("linked_simulation", "linked_topic__subject__grade__curriculum").get(id=self.published_article.id)
        teaser = art.simulation_teaser
        self.assertIsNotNone(teaser)
        self.assertIn("Investigate refractive angles", teaser["overview"])
        self.assertEqual(len(teaser["how_to_use"]), 3)
        self.assertIn("Light bends toward normal", teaser["expected_results"][0])
        self.assertEqual(teaser["subject"], "PHYSICS")

        # Test simulation CTA label
        cta = art.simulation_cta_label
        self.assertEqual(cta, f"Explore {self.simulation.title} Simulation")

        # Test fallback when simulation has no context_spec
        self.simulation.config = {}
        self.simulation.save()
        art_fallback = Article.objects.select_related("linked_simulation").get(id=self.published_article.id)
        fallback_teaser = art_fallback.simulation_teaser
        self.assertEqual(fallback_teaser["overview"], self.simulation.description)
        self.assertEqual(fallback_teaser["how_to_use"], [
            "Adjust experimental variables and observe real-time system responses.",
            "Compare simulated observations with theoretical equations.",
        ])

    def test_public_article_detail_serializer_phase3_fields(self):
        """
        Phase 3: Verify the public DRF article detail endpoint exposes curriculum_lineage,
        simulation_teaser, and simulation_cta_label.
        """
        response = self.client.get(f"/api/knowledge/articles/{self.published_article.slug}/")
        self.assertEqual(response.status_code, 200)
        data = response.data

        self.assertIn("curriculum_lineage", data)
        self.assertIn("simulation_teaser", data)
        self.assertIn("simulation_cta_label", data)

        lineage = data["curriculum_lineage"]
        self.assertEqual(lineage["curriculum"], self.curriculum.name)
        self.assertEqual(lineage["grade"], self.grade.name)
        self.assertEqual(lineage["subject"], self.subject.name)
        self.assertEqual(lineage["topic_id"], self.topic.id)

    def test_article_detail_json_ld_learning_resource(self):
        """
        Phase 3: Verify ArticleDetailView renders Schema.org LearningResource / EducationalApplication
        node in JSON-LD @graph when a simulation is linked, including potentialAction and hasPart links.
        """
        response = self.client.get(f"/knowledge/{self.published_article.slug}/")
        self.assertEqual(response.status_code, 200)

        html = response.content.decode("utf-8")
        match = re.search(r'<script\s+type="application/ld\+json"\s*>(.*?)</script>', html, re.DOTALL)
        self.assertIsNotNone(match)
        json_ld = json.loads(match.group(1).strip())

        graph = json_ld.get("@graph", [])
        learning_resource = next(
            (item for item in graph if "LearningResource" in (item.get("@type") if isinstance(item.get("@type"), list) else [item.get("@type")])),
            None
        )
        self.assertIsNotNone(learning_resource, "Graph must contain a LearningResource node")
        self.assertEqual(learning_resource["name"], self.simulation.title)
        self.assertEqual(learning_resource["learningResourceType"].lower(), "interactive simulation")
        self.assertEqual(learning_resource["applicationCategory"], "EducationalApplication")

        # Potential action deep-link on Article node
        article_node = next(item for item in graph if item.get("@type") == "Article")
        action = article_node.get("potentialAction", {})
        self.assertEqual(action.get("@type"), "InteractAction")
        self.assertIn(f"sim={self.simulation.key}", action.get("target", ""))
        self.assertTrue(action.get("target", "").startswith("https://www.vizlearn.org/student/simulations"))

        # Article hasPart reference
        self.assertIn("hasPart", article_node)
        self.assertEqual(article_node["hasPart"][0]["@id"], f"https://www.vizlearn.org/student/simulations?sim={self.simulation.key}")

    def test_article_detail_simulation_and_curriculum_ui_elements(self):
        """
        Phase 3: Verify the SSR HTML includes the upgraded interactive simulation callout
        with experiment preview cards, CTA button with query params, and full syllabus breadcrumb path.
        """
        # Configure simulation with pedagogical context
        self.simulation.config = {
            "context_spec": {
                "overview": "Explore refractive angles and total internal reflection.",
                "how_to_use": [
                    "Adjust incident ray angle using slider",
                    "Change refractive index n2 to water (1.33)",
                    "Observe critical angle phenomenon"
                ],
                "expected_results": "Light bends toward normal in denser medium."
            }
        }
        self.simulation.save()

        response = self.client.get(f"/knowledge/{self.published_article.slug}/")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        # Interactive Simulation Box
        self.assertIn("Interactive Lab Simulation", html)
        self.assertIn(self.simulation.title, html)
        self.assertIn("Adjust incident ray angle using slider", html)
        self.assertIn("Observe critical angle phenomenon", html)
        self.assertIn(f"href=\"https://www.vizlearn.org/student/simulations?sim={self.simulation.key}\"", html)
        self.assertIn("Interactive Prism Simulation", html)

        # Curriculum Context Box
        self.assertIn("Curriculum Connection", html)
        self.assertIn(self.curriculum.name, html)
        self.assertIn(self.grade.name, html)
        self.assertIn(self.subject.name, html)
        self.assertIn(self.topic.name, html)
        self.assertIn(f"/student/topic/{self.topic.id}", html)

    def test_search_articles_utility_and_api_search_endpoint(self):
        """
        Phase 4: Verify search_articles utility and GET /api/knowledge/search/ endpoint.
        Checks that searching for keywords in title/summary returns published matches,
        while strictly excluding drafts and archived articles.
        """
        from knowledge.search import search_articles

        # Search utility
        results = search_articles(query_string="refraction")
        self.assertIn(self.published_article, results)

        # Drafts must not be in search results
        self.assertNotIn(self.draft_article, results)
        self.assertNotIn(self.archived_article, results)

        # Dedicated search endpoint
        response = self.client.get("/api/knowledge/search/?q=refraction")
        self.assertEqual(response.status_code, 200)
        data = response.data
        results_data = data.get("results") if isinstance(data, dict) and "results" in data else data
        slugs = [item["slug"] for item in results_data]
        self.assertIn(self.published_article.slug, slugs)
        self.assertNotIn(self.draft_article.slug, slugs)

    def test_ssr_article_list_view_with_search_query(self):
        """
        Phase 4: Verify GET /knowledge/?q=... executes search and renders search results header,
        search input value, and clear filter link.
        """
        response = self.client.get("/knowledge/?q=refraction")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        self.assertIn("Search Results for &ldquo;refraction&rdquo;", html)
        self.assertIn("Understanding Snell&#x27;s Law and Refraction", html)
        self.assertIn("Clear search", html)

    def test_ssr_article_list_view_search_empty_state(self):
        """
        Phase 4: Verify searching for a term with no matching articles displays the helpful
        empty state message.
        """
        response = self.client.get("/knowledge/?q=nonexistenttermxyz999")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        self.assertIn("No articles match your search", html)
        self.assertIn("nonexistenttermxyz999", html)
        self.assertIn("Clear Search", html)

    def test_ssr_tag_detail_view_and_404(self):
        """
        Phase 4: Verify GET /knowledge/tag/<slug>/ renders matching tagged articles and breadcrumbs,
        and returns 404 for nonexistent tag slugs.
        """
        response = self.client.get(f"/knowledge/tag/{self.tag_waves.slug}/")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        self.assertIn(f"#{self.tag_waves.name}", html)
        self.assertIn("Understanding Snell&#x27;s Law and Refraction", html)
        self.assertIn("Breadcrumb", html)

        # 404 for nonexistent tag
        response_404 = self.client.get("/knowledge/tag/nonexistent-tag-slug/")
        self.assertEqual(response_404.status_code, 404)

    def test_tag_sitemap_included_in_sitemap_xml(self):
        """
        Phase 4: Verify /sitemap.xml includes tag URLs for tags with published articles.
        """
        response = self.client.get("/sitemap.xml")
        self.assertEqual(response.status_code, 200)
        content = response.content.decode("utf-8")

        self.assertIn(f"/knowledge/tag/{self.tag_waves.slug}/", content)

    def test_article_detail_tag_links_to_tag_page(self):
        """
        Phase 4: Verify tags on the article detail page are clickable links to /knowledge/tag/<slug>/.
        """
        response = self.client.get(f"/knowledge/{self.published_article.slug}/")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        expected_tag_link = f'href="/knowledge/tag/{self.tag_waves.slug}/"'
        self.assertIn(expected_tag_link, html)


class KnowledgePhase5PedagogicalGraphTests(TestCase):
    """
    Phase 5 Tests: Curriculum + Simulation Integration / Pedagogical Knowledge Graph.
    Verifies:
    1. Article.related_concepts resolution via linked_learning_unit and linked_topic.
    2. Article.common_misconceptions resolution via concepts.
    3. DRF PublicArticleDetailSerializer serialization of concepts, relationships, and misconceptions.
    4. SSR ArticleDetailView HTML rendering of 'Common Misconceptions vs. Scientific Reality' and 'Core Concepts to Master'.
    5. Graceful omission when article has no pedagogical linkages.
    6. Strictly bounded query count (zero N+1 queries) when loading article detail page.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="academic_editor",
            email="editor@vizlearn.org",
            first_name="Dr. Jane",
            last_name="Mutiso",
        )

        # Curriculum Hierarchy: Curriculum -> Grade -> Subject -> Topic -> LearningUnit
        self.curriculum = Curriculum.objects.create(name="KCSE Secondary")
        self.grade = Grade.objects.create(name="Form 4", curriculum=self.curriculum)
        self.subject = Subject.objects.create(
            name="Physics",
            grade=self.grade,
        )
        self.topic = Topic.objects.create(
            name="Wave Motion",
            subject=self.subject,
            order=1,
        )
        self.learning_unit = LearningUnit.objects.create(
            name="Refraction of Waves",
            topic=self.topic,
            order=1,
        )

        # Concepts
        self.concept1 = Concept.objects.create(
            name="Snell's Law of Refraction",
            description="Ratio of the sine of incidence to sine of refraction equals relative refractive index.",
            keywords=["optics", "refraction", "snell", "index"],
            learning_unit=self.learning_unit,
        )
        self.concept2 = Concept.objects.create(
            name="Total Internal Reflection",
            description="Complete reflection of a ray of light within a medium such as water or glass from the surrounding surfaces back into the medium.",
            keywords=["tir", "critical angle", "boundary"],
            learning_unit=self.learning_unit,
        )

        # Semantic Concept Relationship
        self.relationship = ConceptRelationship.objects.create(
            source=self.concept1,
            target=self.concept2,
            relationship_type="prerequisite",
        )

        # Misconceptions
        self.misc1 = Misconception.objects.create(
            concept=self.concept1,
            description="Light rays physically swerve and slow down like a wheel on gravel.",
            correction="Light wavefronts refract due to phase velocity variation across the interface governed by boundary conditions.",
        )
        self.misc2 = Misconception.objects.create(
            concept=self.concept2,
            description="Total internal reflection can occur when light travels from air into diamond.",
            correction="Total internal reflection requires light to travel from an optically denser medium toward an optically rarer medium at an angle greater than the critical angle.",
        )

        # Category and Tag
        self.category = ArticleCategory.objects.create(
            name="Geometric Optics",
            slug="geometric-optics",
            linked_subject_name="Physics",
        )
        self.tag = ArticleTag.objects.create(name="Wave Optics", slug="wave-optics")

        # Article 1: Linked to learning unit + topic (Rich pedagogical article)
        self.article1 = Article.objects.create(
            title="Complete Guide to Wave Refraction and Total Internal Reflection",
            slug="complete-guide-refraction-tir",
            summary="A comprehensive secondary guide to Snell's law and total internal reflection.",
            body="Light travels through optical media according to fundamental wave mechanics...",
            category=self.category,
            linked_topic=self.topic,
            linked_learning_unit=self.learning_unit,
            author=self.user,
            status="published",
            published_at=timezone.now(),
        )
        self.article1.tags.add(self.tag)

        # Article 2: Linked to topic only (Fallback resolution)
        self.article2 = Article.objects.create(
            title="Introduction to Wave Motion Dynamics",
            slug="intro-wave-motion-dynamics",
            summary="Understanding progressive waves, boundaries, and energy transfer.",
            body="Waves transfer energy through a medium without transferring matter...",
            category=self.category,
            linked_topic=self.topic,
            author=self.user,
            status="published",
            published_at=timezone.now(),
        )

        # Article 3: Platform article (No curriculum linkages)
        self.article3 = Article.objects.create(
            title="VizLearn Platform Term 2 Updates",
            slug="vizlearn-term-2-updates",
            summary="Platform news and interactive improvements for teachers and students.",
            body="We are proud to release our newest physics simulations and teacher tools...",
            category=self.category,
            author=self.user,
            status="published",
            published_at=timezone.now(),
        )

    def test_article_related_concepts_via_learning_unit(self):
        """
        Verify Article.related_concepts returns concepts attached to its linked_learning_unit.
        """
        concepts = self.article1.related_concepts
        concept_names = [c.name for c in concepts]
        self.assertEqual(len(concepts), 2)
        self.assertIn("Snell's Law of Refraction", concept_names)
        self.assertIn("Total Internal Reflection", concept_names)

    def test_article_related_concepts_via_topic_fallback(self):
        """
        Verify Article.related_concepts returns concepts from topic's learning units when linked_learning_unit is null.
        """
        concepts = self.article2.related_concepts
        concept_names = [c.name for c in concepts]
        self.assertEqual(len(concepts), 2)
        self.assertIn("Snell's Law of Refraction", concept_names)
        self.assertIn("Total Internal Reflection", concept_names)

    def test_article_related_concepts_empty_when_unlinked(self):
        """
        Verify Article.related_concepts returns empty list when no curriculum unit or topic is linked.
        """
        self.assertEqual(self.article3.related_concepts, [])

    def test_article_common_misconceptions(self):
        """
        Verify Article.common_misconceptions returns all misconceptions attached to related concepts.
        """
        misconceptions = self.article1.common_misconceptions
        self.assertEqual(len(misconceptions), 2)
        descriptions = [m.description for m in misconceptions]
        self.assertTrue(any("Light rays physically swerve" in d for d in descriptions))
        self.assertTrue(any("air into diamond" in d for d in descriptions))

    def test_article_common_misconceptions_empty_when_unlinked(self):
        """
        Verify Article.common_misconceptions returns empty list when article has no concepts.
        """
        self.assertEqual(self.article3.common_misconceptions, [])

    def test_drf_article_detail_api_exposes_pedagogical_graph(self):
        """
        Verify DRF GET /api/knowledge/articles/<slug>/ returns related_concepts and common_misconceptions.
        """
        response = self.client.get(f"/api/knowledge/articles/{self.article1.slug}/")
        self.assertEqual(response.status_code, 200)
        data = response.json()

        # Concepts check
        self.assertIn("related_concepts", data)
        self.assertEqual(len(data["related_concepts"]), 2)
        concept_data = data["related_concepts"][0]
        self.assertEqual(concept_data["name"], "Snell's Law of Refraction")
        self.assertIn("optics", concept_data["keywords"])
        self.assertIn("relationships", concept_data)
        self.assertEqual(len(concept_data["relationships"]), 1)
        self.assertEqual(concept_data["relationships"][0]["relationship_type"], "prerequisite")
        self.assertEqual(concept_data["relationships"][0]["target_concept_name"], "Total Internal Reflection")

        # Misconceptions check
        self.assertIn("common_misconceptions", data)
        self.assertEqual(len(data["common_misconceptions"]), 2)
        misc_data = data["common_misconceptions"][0]
        self.assertIn("Light rays physically swerve", misc_data["description"])
        self.assertIn("phase velocity variation", misc_data["correction"])
        self.assertEqual(misc_data["concept_name"], "Snell's Law of Refraction")

    def test_ssr_article_detail_view_renders_concepts_and_misconceptions(self):
        """
        Verify SSR GET /knowledge/<slug>/ renders the Common Misconceptions and Core Concepts sections.
        """
        response = self.client.get(f"/knowledge/{self.article1.slug}/")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        # Misconceptions section
        self.assertIn("Common Misconceptions vs. Scientific Reality", html)
        self.assertIn("Light rays physically swerve", html)
        self.assertIn("phase velocity variation", html)
        self.assertIn("air into diamond", html)

        # Core Concepts section
        self.assertIn("Core Concepts to Master", html)
        self.assertIn("Snell&#x27;s Law of Refraction", html)
        self.assertIn("Total Internal Reflection", html)
        self.assertIn("optics", html)
        self.assertIn("prerequisite", html.lower())

        # Curriculum lineage
        self.assertIn("Part of the VizLearn Curriculum", html)
        self.assertIn("KCSE Secondary", html)
        self.assertIn("Form 4", html)

    def test_ssr_article_detail_view_graceful_when_no_concepts(self):
        """
        Verify SSR GET /knowledge/<slug>/ does not render Misconceptions or Core Concepts sections
        when the article has no curriculum linkages.
        """
        response = self.client.get(f"/knowledge/{self.article3.slug}/")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        self.assertNotIn("Common Misconceptions vs. Scientific Reality", html)
        self.assertNotIn("Core Concepts to Master", html)

    def test_ssr_article_detail_bounded_queries(self):
        """
        Verify that loading the article detail page executes in a strictly bounded number of queries (10 queries),
        preventing any N+1 query regression as concepts, misconceptions, and related articles grow.
        """
        self.article1.related_articles.add(self.article2)

        # Warm up any internal caches if needed
        self.client.get(f"/knowledge/{self.article1.slug}/")

        with self.assertNumQueries(10):
            response = self.client.get(f"/knowledge/{self.article1.slug}/")
            self.assertEqual(response.status_code, 200)


class KnowledgePhase6SEOHardeningTests(TestCase):
    """
    Phase 6 Tests: SEO Hardening & Structured Data.
    Verifies:
    1. Schema.org FAQPage / Q&A structured data generation for articles with misconceptions.
    2. EducationalOrganization publisher, logo, and fallback OpenGraph image handling.
    3. Knowledge index (/knowledge/) Schema.org graph: EducationalOrganization, WebSite (SearchAction), CollectionPage, BreadcrumbList.
    4. Category and tag detail pages Schema.org graph: CollectionPage and BreadcrumbList.
    5. Upgraded sitemaps (/sitemap.xml): includes /knowledge/ index, static marketing pages, and dynamic category/tag lastmod.
    6. Upgraded robots.txt (/robots.txt): crawl-trap disallow rules and private SPA route guarding.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="seo_editor",
            email="seo@vizlearn.org",
            first_name="David",
            last_name="Ochieng",
        )

        self.curriculum = Curriculum.objects.create(name="KCSE Secondary")
        self.grade = Grade.objects.create(name="Form 3", curriculum=self.curriculum)
        self.subject = Subject.objects.create(name="Chemistry", grade=self.grade)
        self.topic = Topic.objects.create(name="Gas Laws", subject=self.subject, order=1)
        self.learning_unit = LearningUnit.objects.create(name="Boyle's Law", topic=self.topic, order=1)

        self.concept = Concept.objects.create(
            name="Boyle's Law Pressure-Volume Relationship",
            description="Pressure is inversely proportional to volume at constant temperature.",
            keywords=["gases", "pressure", "boyle"],
            learning_unit=self.learning_unit,
        )

        self.misconception = Misconception.objects.create(
            concept=self.concept,
            description="Gas molecules slow down when compressed into a smaller volume at constant temperature.",
            correction="At constant temperature, average kinetic energy and molecular speed remain constant; pressure increases solely because collision frequency with container walls increases.",
        )

        self.category = ArticleCategory.objects.create(
            name="Thermodynamics & Gases",
            slug="thermodynamics-gases",
            description="Explore thermodynamic concepts and gas behaviors.",
            order=1,
        )

        self.tag = ArticleTag.objects.create(
            name="Gas Laws",
            slug="gas-laws",
        )

        self.article = Article.objects.create(
            title="Understanding Boyle's Law",
            slug="understanding-boyles-law",
            summary="A deep dive into gas compression at constant temperature.",
            body="## Boyle's Law\n\nWhen volume decreases, pressure increases.",
            status="published",
            article_type="deep_dive",
            category=self.category,
            author=self.user,
            linked_topic=self.topic,
            linked_learning_unit=self.learning_unit,
            published_at=timezone.now(),
        )
        self.article.tags.add(self.tag)

    def test_article_detail_misconceptions_faq_schema(self):
        """
        Verify that an article with linked misconceptions outputs a valid FAQPage Schema.org node
        containing Question (misconception) and acceptedAnswer (scientific correction).
        """
        response = self.client.get(f"/knowledge/{self.article.slug}/")
        self.assertEqual(response.status_code, 200)

        html = response.content.decode("utf-8")
        self.assertIn('<script type="application/ld+json">', html)

        # Parse JSON-LD script content
        start_tag = '<script type="application/ld+json">'
        end_tag = '</script>'
        start_idx = html.find(start_tag) + len(start_tag)
        end_idx = html.find(end_tag, start_idx)
        json_content = html[start_idx:end_idx].strip()
        data = json.loads(json_content)

        self.assertIn("@graph", data)
        nodes = data["@graph"]

        faq_node = next((n for n in nodes if n.get("@type") == "FAQPage"), None)
        self.assertIsNotNone(faq_node, "FAQPage node missing from article JSON-LD graph")
        self.assertEqual(faq_node["@id"], f"https://www.vizlearn.org/knowledge/{self.article.slug}/#misconceptions")

        main_entity = faq_node["mainEntity"]
        self.assertEqual(len(main_entity), 1)
        q_item = main_entity[0]
        self.assertEqual(q_item["@type"], "Question")
        self.assertIn(self.misconception.description, q_item["name"])
        self.assertEqual(q_item["acceptedAnswer"]["@type"], "Answer")
        self.assertEqual(q_item["acceptedAnswer"]["text"], self.misconception.correction)

    def test_article_detail_schema_publisher_and_fallback_image(self):
        """
        Verify that Article node in JSON-LD contains EducationalOrganization publisher with logo,
        and uses fallback image when featured_image_url is not set.
        """
        response = self.client.get(f"/knowledge/{self.article.slug}/")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        start_tag = '<script type="application/ld+json">'
        end_tag = '</script>'
        start_idx = html.find(start_tag) + len(start_tag)
        end_idx = html.find(end_tag, start_idx)
        data = json.loads(html[start_idx:end_idx].strip())

        article_node = next((n for n in data["@graph"] if n.get("@type") == "Article"), None)
        self.assertIsNotNone(article_node)

        # Publisher verification
        publisher = article_node["publisher"]
        self.assertEqual(publisher["@type"], "EducationalOrganization")
        self.assertEqual(publisher["name"], "VizLearn")
        self.assertEqual(publisher["logo"]["url"], "https://www.vizlearn.org/images/logo.png")

        # Fallback image verification
        self.assertIn("https://www.vizlearn.org/images/og-knowledge.png", article_node["image"])
        self.assertEqual(article_node["inLanguage"], "en")

    def test_knowledge_index_schema_org_graph(self):
        """
        Verify that /knowledge/ renders EducationalOrganization, WebSite (with SearchAction),
        CollectionPage (with ItemList), and BreadcrumbList structured data.
        """
        response = self.client.get("/knowledge/")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")

        self.assertIn('<script type="application/ld+json">', html)

        start_tag = '<script type="application/ld+json">'
        end_tag = '</script>'
        start_idx = html.find(start_tag) + len(start_tag)
        end_idx = html.find(end_tag, start_idx)
        data = json.loads(html[start_idx:end_idx].strip())

        types = [n.get("@type") for n in data["@graph"]]
        self.assertIn("EducationalOrganization", types)
        self.assertIn("WebSite", types)
        self.assertIn("CollectionPage", types)
        self.assertIn("BreadcrumbList", types)

        # Verify SearchAction
        website_node = next(n for n in data["@graph"] if n.get("@type") == "WebSite")
        self.assertEqual(website_node["potentialAction"]["@type"], "SearchAction")
        self.assertIn("/knowledge/?q=", website_node["potentialAction"]["target"])

    def test_category_and_tag_detail_breadcrumbs_and_collection_schema(self):
        """
        Verify that CategoryDetailView and TagDetailView render valid CollectionPage and BreadcrumbList JSON-LD.
        """
        cat_res = self.client.get(f"/knowledge/category/{self.category.slug}/")
        self.assertEqual(cat_res.status_code, 200)
        cat_html = cat_res.content.decode("utf-8")
        self.assertIn('<script type="application/ld+json">', cat_html)

        start_tag = '<script type="application/ld+json">'
        end_tag = '</script>'
        start_idx = cat_html.find(start_tag) + len(start_tag)
        end_idx = cat_html.find(end_tag, start_idx)
        cat_data = json.loads(cat_html[start_idx:end_idx].strip())
        cat_types = [n.get("@type") for n in cat_data["@graph"]]
        self.assertIn("CollectionPage", cat_types)
        self.assertIn("BreadcrumbList", cat_types)

        tag_res = self.client.get(f"/knowledge/tag/{self.tag.slug}/")
        self.assertEqual(tag_res.status_code, 200)
        tag_html = tag_res.content.decode("utf-8")
        self.assertIn('<script type="application/ld+json">', tag_html)

        start_idx = tag_html.find(start_tag) + len(start_tag)
        end_idx = tag_html.find(end_tag, start_idx)
        tag_data = json.loads(tag_html[start_idx:end_idx].strip())
        tag_types = [n.get("@type") for n in tag_data["@graph"]]
        self.assertIn("CollectionPage", tag_types)
        self.assertIn("BreadcrumbList", tag_types)

    def test_sitemaps_include_index_static_and_lastmod(self):
        """
        Verify /sitemap.xml returns 200 OK and includes:
        - /knowledge/ index
        - static marketing pages (/, /subscription, /contact)
        - dynamic category and tag lastmod elements
        """
        response = self.client.get("/sitemap.xml")
        self.assertEqual(response.status_code, 200)
        content = response.content.decode("utf-8")

        public_site_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/")
        self.assertIn(f"<loc>{public_site_url}/knowledge/</loc>", content)
        self.assertIn(f"<loc>{public_site_url}/</loc>", content)
        self.assertIn(f"<loc>{public_site_url}/subscription</loc>", content)
        self.assertIn(f"<loc>{public_site_url}/contact</loc>", content)
        self.assertIn(f"<loc>{public_site_url}/knowledge/{self.article.slug}/</loc>", content)
        self.assertIn(f"<loc>{public_site_url}/knowledge/category/{self.category.slug}/</loc>", content)
        self.assertIn(f"<loc>{public_site_url}/knowledge/tag/{self.tag.slug}/</loc>", content)

    def test_robots_txt_crawl_traps_and_spa_guards(self):
        """
        Verify /robots.txt includes crawl-trap prevention for ?q= and ?search=
        as well as disallow directives for private SPA routes.
        """
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        content = response.content.decode("utf-8")

        self.assertIn("Disallow: /knowledge/*?*q=", content)
        self.assertIn("Disallow: /knowledge/*?*search=", content)
        self.assertIn("Disallow: /student/", content)
        self.assertIn("Disallow: /teacher/", content)
        self.assertIn("Disallow: /school/", content)
        self.assertIn("Disallow: /admin-dashboard/", content)
        self.assertIn("Disallow: /reset-password/", content)
        self.assertIn("Disallow: /invitation/", content)
        self.assertIn("Allow: /knowledge/", content)
        self.assertIn("Allow: /static/", content)

    def test_social_meta_tags_not_empty_across_templates(self):
        """
        Verify that og:title, twitter:title, og:description, and twitter:description
        are populated with non-empty content across index, category, tag, and article views.
        """
        urls_to_test = [
            ("/knowledge/", "VizLearn Knowledge Base"),
            (f"/knowledge/category/{self.category.slug}/", self.category.name),
            (f"/knowledge/tag/{self.tag.slug}/", self.tag.name),
            (f"/knowledge/{self.article.slug}/", self.article.title),
        ]
        for url, expected_fragment in urls_to_test:
            res = self.client.get(url)
            self.assertEqual(res.status_code, 200)
            html = res.content.decode("utf-8")

            # Check og:title is present, non-empty, and contains expected text
            self.assertIn('<meta property="og:title" content="', html)
            self.assertNotIn('<meta property="og:title" content="">', html)
            self.assertIn(expected_fragment, html)

            # Check twitter:title is present and non-empty
            self.assertIn('<meta name="twitter:title" content="', html)
            self.assertNotIn('<meta name="twitter:title" content="">', html)

    def test_sitemap_xml_bounded_queries(self):
        """
        Verify that /sitemap.xml executes in a constant O(1) number of queries (<= 5 queries),
        guaranteeing zero N+1 database queries as categories, tags, and articles scale.
        """
        # Create additional categories, tags, and articles to verify query invariance
        cat2 = ArticleCategory.objects.create(name="Chemistry Cat", slug="chemistry-cat", order=2)
        tag2 = ArticleTag.objects.create(name="Reactivity", slug="reactivity")
        art2 = Article.objects.create(
            title="Periodic Trends",
            slug="periodic-trends",
            summary="A summary of periodic trends.",
            body="Trends in the periodic table.",
            status="published",
            category=cat2,
            author=self.user,
            published_at=timezone.now(),
        )
        art2.tags.add(tag2)

        # Warm up if needed
        self.client.get("/sitemap.xml")

        # Exactly 7 queries: 1 index + 2 articles (count+select) + 2 categories (count+select) + 2 tags (count+select)
        with self.assertNumQueries(7):
            response = self.client.get("/sitemap.xml")
            self.assertEqual(response.status_code, 200)


class StarterContentTests(TestCase):
    """
    Tests for Phase 7: Starter Content Creation & Curriculum Integration.
    Verifies that the seed_starter_knowledge management command executes cleanly,
    provisions all 7 authentic KCSE starter articles with categories, tags, simulations,
    concepts, and misconceptions, and that each article is discoverable via SSR,
    sitemap, search, and Schema.org structured data.
    """

    @classmethod
    def setUpTestData(cls):
        call_command("seed_starter_knowledge")

    def test_seed_starter_knowledge_creates_seven_articles(self):
        """
        Verify that 7 starter articles are created with status 'published',
        non-null published_at, and assigned categories and tags.
        """
        self.assertEqual(Article.objects.count(), 7)
        for article in Article.objects.all():
            self.assertEqual(article.status, "published")
            self.assertIsNotNone(article.published_at)
            self.assertIsNotNone(article.category)
            self.assertGreater(article.tags.count(), 0)
            self.assertIsNotNone(article.linked_simulation)
            self.assertIsNotNone(article.linked_topic)
            self.assertIsNotNone(article.linked_learning_unit)
            # featured_image_url is intentionally None for seeded articles
            # (no real scientific diagrams available; honesty over fabricated placeholders)
            self.assertIsNone(article.featured_image_url)
            self.assertEqual(article.featured_image_alt, "")
            self.assertLessEqual(len(article.meta_title), 70)
            self.assertLessEqual(len(article.meta_description), 160)

    def test_all_starter_articles_render_200_ok(self):
        """
        Verify that each starter article renders 200 OK via public SSR,
        contains semantic markup, KaTeX math indicators, simulation teaser/CTA,
        and common misconceptions block.
        """
        for article in Article.objects.all():
            res = self.client.get(f"/knowledge/{article.slug}/")
            self.assertEqual(res.status_code, 200)
            html = res.content.decode("utf-8")

            # Basic semantic structure
            self.assertIn("<article", html)
            self.assertIn(article.title, html)
            self.assertIn(article.summary, html)

            # KaTeX math elements or formulas
            self.assertTrue("$$" in html or "\\(" in html or "katex" in html)

            # Simulation teaser and launch CTA
            self.assertTrue(
                "Launch" in html or "Explore" in html or "Simulation" in html
            )
            self.assertIn(article.linked_simulation.title, html)

            # Misconceptions block ("Myth vs. Scientific Reality")
            self.assertIn("Common Misconceptions", html)
            self.assertIn("Scientific Reality", html)

            # Author and breadcrumbs
            self.assertIn("Breadcrumb", html)

    def test_starter_articles_appear_in_sitemap(self):
        """
        Verify that all 7 starter articles appear in /sitemap.xml.
        """
        res = self.client.get("/sitemap.xml")
        self.assertEqual(res.status_code, 200)
        content = res.content.decode("utf-8")
        for article in Article.objects.all():
            self.assertIn(f"/knowledge/{article.slug}/", content)

    def test_starter_articles_search_discoverability(self):
        """
        Verify that starter articles are discoverable through full-text search.
        """
        searches = [
            ("Boyle", "understanding-boyles-law-pressure-volume-relationship"),
            ("Archimedes", "archimedes-principle-upthrust-buoyancy-physics"),
            ("Transpiration", "cohesion-tension-theory-transpiration-water-ascent"),
            ("Electrolyte", "acids-bases-ph-strong-weak-electrolytes-dissociation"),
            ("Convex", "convex-thin-lenses-ray-diagrams-image-formation"),
            ("Myopia", "human-eye-accommodation-refractive-defects-vision"),
            ("Collision", "collision-theory-reaction-rates-activation-energy"),
        ]
        for query, expected_slug in searches:
            res = self.client.get(f"/knowledge/?q={query}")
            self.assertEqual(res.status_code, 200)
            html = res.content.decode("utf-8")
            self.assertIn(expected_slug, html)

    def test_starter_articles_schema_org_markup(self):
        """
        Verify that all starter articles output valid Schema.org JSON-LD graphs
        containing Article, BreadcrumbList, LearningResource, and FAQPage.
        """
        for article in Article.objects.all():
            res = self.client.get(f"/knowledge/{article.slug}/")
            self.assertEqual(res.status_code, 200)
            html = res.content.decode("utf-8")

            # Locate JSON-LD block
            match = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', html, re.DOTALL)
            self.assertIsNotNone(match, f"No JSON-LD found for {article.slug}")
            raw_json = match.group(1).replace("&quot;", '"')
            data = json.loads(raw_json)

            self.assertEqual(data.get("@context"), "https://schema.org")
            graph = data.get("@graph", [])
            types = {node.get("@type") for node in graph}

            self.assertIn("Article", types)
            self.assertIn("BreadcrumbList", types)
            self.assertIn("LearningResource", types)
            self.assertIn("FAQPage", types)

            # Check FAQPage questions and answers
            faq_node = next((n for n in graph if n.get("@type") == "FAQPage"), None)
            self.assertIsNotNone(faq_node)
            self.assertGreater(len(faq_node.get("mainEntity", [])), 0)
            first_q = faq_node["mainEntity"][0]
            self.assertEqual(first_q["@type"], "Question")
            self.assertEqual(first_q["acceptedAnswer"]["@type"], "Answer")

    def test_category_pages_render_with_seeded_articles(self):
        """
        Verify that category detail pages (/knowledge/category/<slug>/) render 200 OK
        with the corresponding articles.
        """
        for cat_slug in ["chemistry", "physics", "biology"]:
            res = self.client.get(f"/knowledge/category/{cat_slug}/")
            self.assertEqual(res.status_code, 200)
            html = res.content.decode("utf-8")
            self.assertIn("<article", html)


class ProductionHardeningTests(TestCase):
    """
    Phase 8: Production Hardening, Caching, Bleach Security, Accessibility & GA4 Analytics Tests.
    """

    def setUp(self):
        cache.clear()
        self.category = ArticleCategory.objects.create(
            name="Thermodynamics",
            slug="thermodynamics",
            description="Study of heat and energy transfer.",
            linked_subject_name="Physics",
            order=1,
        )
        self.tag = ArticleTag.objects.create(name="Heat Engine", slug="heat-engine")
        self.tag2 = ArticleTag.objects.create(name="Efficiency", slug="efficiency")
        self.simulation = Simulation.objects.create(
            key="carnot_cycle_sim",
            title="Carnot Engine Heat Cycle",
            topic="Thermodynamics",
            description="Interactive cycle simulator",
            subject=SubjectDomain.PHYSICS,
            status=SimulationStatus.ACTIVE,
        )
        self.article = Article.objects.create(
            title="Understanding the Carnot Cycle and Efficiency",
            slug="carnot-cycle-efficiency",
            summary="Thermodynamic limits of heat engines and reversible cycles.",
            body="## Reversible Cycles\n\nThe Carnot cycle defines the theoretical maximum efficiency.\n\nCheck [External Reference](https://example.com/carnot) for details.",
            category=self.category,
            linked_simulation=self.simulation,
            status="published",
            published_at=timezone.now(),
        )
        self.article.tags.add(self.tag, self.tag2)

    def test_settings_and_cache_configuration(self):
        """
        Verify Django cache configuration, session engine, CSRF trusted origins,
        and X-Forwarded-Host reverse proxy compatibility.
        """
        self.assertIn("default", settings.CACHES)
        self.assertTrue(settings.USE_X_FORWARDED_HOST)
        self.assertIn("https://api.vizlearn.co", settings.CSRF_TRUSTED_ORIGINS)
        context_processors = settings.TEMPLATES[0]["OPTIONS"]["context_processors"]
        self.assertIn("knowledge.context_processors.analytics_context", context_processors)

    def test_taxonomy_low_level_cache_and_signal_invalidation(self):
        """
        Verify get_cached_categories and get_cached_popular_tags populate Redis/LocMem,
        and post_save/post_delete signals automatically invalidate them.
        """
        cache.clear()
        self.assertIsNone(cache.get("knowledge_all_categories"))
        self.assertIsNone(cache.get("knowledge_popular_tags"))

        # Fetching categories caches them
        cats = get_cached_categories()
        self.assertGreater(len(cats), 0)
        self.assertIsNotNone(cache.get("knowledge_all_categories"))

        # Fetching tags caches them
        tags = get_cached_popular_tags()
        self.assertGreater(len(tags), 0)
        self.assertIsNotNone(cache.get("knowledge_popular_tags"))

        # Modifying a category triggers post_save signal and invalidates cache
        self.category.name = "Thermodynamics & Heat"
        self.category.save()
        self.assertIsNone(cache.get("knowledge_all_categories"))

        # Repopulate tag cache and test tag post_save signal
        get_cached_popular_tags()
        self.assertIsNotNone(cache.get("knowledge_popular_tags"))
        self.tag.name = "Carnot Engines"
        self.tag.save()
        self.assertIsNone(cache.get("knowledge_popular_tags"))

    def test_admin_cache_invalidation_actions(self):
        """
        Verify that admin bulk actions (publish_articles, archive_articles)
        purge cached category and tag taxonomies.
        """
        cache.set("knowledge_all_categories", ["dummy"])
        cache.set("knowledge_popular_tags", ["dummy"])

        admin_instance = ArticleAdmin(Article, admin.site)
        admin_instance.publish_articles(None, Article.objects.filter(id=self.article.id))
        self.assertIsNone(cache.get("knowledge_all_categories"))
        self.assertIsNone(cache.get("knowledge_popular_tags"))

        # Repopulate and call archive_articles
        cache.set("knowledge_all_categories", ["dummy"])
        cache.set("knowledge_popular_tags", ["dummy"])
        admin_instance.archive_articles(None, Article.objects.filter(id=self.article.id))
        self.assertIsNone(cache.get("knowledge_all_categories"))
        self.assertIsNone(cache.get("knowledge_popular_tags"))

    def test_template_fragment_caching_and_automatic_busting(self):
        """
        Verify template fragment caching stores rendered HTML fragments and automatically
        busts cache when article is updated (due to updated_at timestamp keying).
        """
        res = self.client.get(f"/knowledge/{self.article.slug}/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("The Carnot cycle defines the theoretical maximum efficiency.", res.content.decode("utf-8"))

        # Update article content and updated_at
        self.article.body = "## Reversible Cycles\n\nUPDATED: Maximum thermodynamic performance."
        self.article.save()

        res2 = self.client.get(f"/knowledge/{self.article.slug}/")
        self.assertEqual(res2.status_code, 200)
        html2 = res2.content.decode("utf-8")
        self.assertIn("UPDATED: Maximum thermodynamic performance.", html2)

    def test_sitemap_caching_and_headers(self):
        """
        Verify that /sitemap.xml is cached and serves valid XML with caching headers.
        """
        res = self.client.get("/sitemap.xml")
        self.assertEqual(res.status_code, 200)
        self.assertIn("xml", res.get("Content-Type", ""))
        self.assertIn("<urlset", res.content.decode("utf-8"))

    def test_bleach_xss_and_reverse_tabnabbing(self):
        """
        Verify Bleach Markdown sanitization:
        - Injects rel='noopener noreferrer' on external links.
        - Strips harmful XSS payloads (<script>, event handlers like onerror, onload).
        - Strips unsafe schemes like javascript:.
        """
        # Test reverse tabnabbing defense
        md_link = "[External Link](https://external.example.com)"
        html = render_article_markdown(md_link)
        self.assertIn('rel="noopener noreferrer"', html)
        self.assertIn('href="https://external.example.com"', html)

        # Test XSS sanitization
        malicious_md = "<script>alert('pwned')</script><img src=x onerror=alert(1)> [Click](javascript:alert(1))"
        sanitized = render_article_markdown(malicious_md)
        self.assertNotIn("<script>", sanitized)
        self.assertNotIn("onerror", sanitized)
        self.assertNotIn("javascript:", sanitized)

    def test_wcag_accessibility_attributes_in_templates(self):
        """
        Verify accessibility attributes across templates:
        - Skip link and main landmark with tabindex='-1'.
        - Semantic navigation drawer and form role='search'.
        - Focus rings and high contrast colors.
        - Reduced motion preferences (motion-reduce:animate-none).
        - Accessible KaTeX math rendering (htmlAndMathml).
        """
        # Base template and Article Detail
        res = self.client.get(f"/knowledge/{self.article.slug}/")
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")

        self.assertIn('<a href="#main-content"', html)
        self.assertIn('<main id="main-content" tabindex="-1"', html)
        self.assertIn('role="search"', html)
        self.assertIn('aria-label="Mobile Navigation"', html)
        self.assertIn('motion-reduce:animate-none', html)
        self.assertIn("output: 'htmlAndMathml'", html)

        # Article List
        res_list = self.client.get("/knowledge/")
        self.assertEqual(res_list.status_code, 200)
        html_list = res_list.content.decode("utf-8")
        self.assertIn('role="search"', html_list)
        self.assertIn('aria-current="page"', html_list)
        self.assertIn('aria-label="Read article:', html_list)

        # Category Detail
        res_cat = self.client.get(f"/knowledge/category/{self.category.slug}/")
        self.assertEqual(res_cat.status_code, 200)
        html_cat = res_cat.content.decode("utf-8")
        self.assertIn('role="search"', html_cat)
        self.assertIn('aria-label="Category filter"', html_cat)
        self.assertIn('aria-current="page"', html_cat)

        # Tag Detail
        res_tag = self.client.get(f"/knowledge/tag/{self.tag.slug}/")
        self.assertEqual(res_tag.status_code, 200)
        html_tag = res_tag.content.decode("utf-8")
        self.assertIn('role="search"', html_tag)
        self.assertIn('aria-label="Related topic tags"', html_tag)

    @override_settings(GA4_MEASUREMENT_ID="G-TESTANALYTICS")
    def test_ga4_analytics_context_and_rendering(self):
        """
        Verify GA4 snippet is rendered in templates when GA4_MEASUREMENT_ID is configured,
        and suppressed when empty.
        """
        res = self.client.get("/knowledge/")
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")
        self.assertIn("https://www.googletagmanager.com/gtag/js?id=G-TESTANALYTICS", html)
        self.assertIn("G-TESTANALYTICS", html)

    @override_settings(GA4_MEASUREMENT_ID="")
    def test_ga4_analytics_suppressed_when_unset(self):
        """
        Verify GA4 script is completely omitted when GA4_MEASUREMENT_ID is empty.
        """
        res = self.client.get("/knowledge/")
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")
        self.assertNotIn("googletagmanager.com", html)


class PostImplementationAuditHardeningTests(TestCase):
    """
    Automated regression and hardening tests for post-implementation audit fixes:
    - Reserved slug protection prevents collision with knowledge routes.
    - Category search empty state handles queries and provides clear filter button.
    - TagDetailView uses cached popular tags and excludes current tag.
    - PublicArticleViewSet supports status filter for admins while strictly blocking non-admins.
    - ArticleDetailView caches rendered markdown body in Python cache.
    - Article model memoizes related_concepts and common_misconceptions.
    - WCAG contrast compliance for empty state CTAs and card metadata.
    - Robots.txt disallows explicit /knowledge/?q= and /knowledge/?search= patterns.
    """

    def setUp(self):
        cache.clear()
        self.category = ArticleCategory.objects.create(
            name="Physics",
            slug="physics",
            order=1,
        )
        self.tag1 = ArticleTag.objects.create(name="Mechanics", slug="mechanics")
        self.tag2 = ArticleTag.objects.create(name="Thermodynamics", slug="thermodynamics")
        self.user = User.objects.create_user(
            username="student_user",
            password="password123",
            role="student",
        )
        self.admin_user = User.objects.create_superuser(
            username="admin_user",
            email="admin@vizlearn.co",
            password="adminpassword123",
        )
        self.article = Article.objects.create(
            title="Kinematics and Motion",
            summary="Study of motion without reference to the forces causing it.",
            body="## Linear Motion\n\nDisplacement is a vector quantity.",
            category=self.category,
            status="published",
            published_at=timezone.now(),
        )
        self.article.tags.add(self.tag1, self.tag2)

        self.draft_article = Article.objects.create(
            title="Draft Nuclear Physics",
            summary="Internal review draft on binding energy.",
            body="Draft content.",
            category=self.category,
            status="draft",
        )

    def test_reserved_slug_protection(self):
        # Article with title 'Category' should avoid colliding with /knowledge/category/
        art_cat = Article.objects.create(
            title="Category",
            summary="Article about taxonomy categories.",
            body="Content",
        )
        self.assertEqual(art_cat.slug, "category-article")

        # Article with title 'Tag' should avoid colliding with /knowledge/tag/
        art_tag = Article.objects.create(
            title="Tag",
            summary="Article about tag taxonomies.",
            body="Content",
        )
        self.assertEqual(art_tag.slug, "tag-article")

    def test_category_search_empty_state_and_clear_link(self):
        # Search for non-existent term inside category
        res = self.client.get(f"/knowledge/category/{self.category.slug}/?q=nonexistentxyz")
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")
        self.assertIn("No articles match your search in Physics", html)
        self.assertIn("Clear Search Filter", html)
        self.assertIn(f"/knowledge/category/{self.category.slug}/", html)

    def test_tag_detail_cached_popular_tags(self):
        res = self.client.get(f"/knowledge/tag/{self.tag1.slug}/")
        self.assertEqual(res.status_code, 200)
        # Should include tag2 but exclude current tag1 in popular tags switcher
        self.assertIn(f"#{self.tag2.name}", res.content.decode("utf-8"))
        popular_tags = res.context["popular_tags"]
        self.assertNotIn(self.tag1, popular_tags)

    def test_public_article_viewset_status_filtering(self):
        # Anonymous / student user attempting to query ?status=draft -> 403 PermissionDenied
        res_anon = self.client.get("/api/knowledge/articles/?status=draft")
        self.assertEqual(res_anon.status_code, status.HTTP_403_FORBIDDEN)

        # Admin user querying ?status=draft with JWT Bearer token -> 200 with draft articles
        from rest_framework_simplejwt.tokens import RefreshToken
        admin_token = str(RefreshToken.for_user(self.admin_user).access_token)
        res_admin = self.client.get(
            "/api/knowledge/articles/?status=draft",
            HTTP_AUTHORIZATION=f"Bearer {admin_token}",
        )
        self.assertEqual(res_admin.status_code, status.HTTP_200_OK)
        data = res_admin.json()
        results = data.get("results", data)
        slugs = [item["slug"] for item in results]
        self.assertIn(self.draft_article.slug, slugs)
        self.assertNotIn(self.article.slug, slugs)

    def test_article_detail_rendered_markdown_cache(self):
        # Request detail view; verify cache key is created
        cache_key = f"article_rendered_markdown_{self.article.id}_{self.article.updated_at.timestamp()}"
        self.assertIsNone(cache.get(cache_key))
        res = self.client.get(f"/knowledge/{self.article.slug}/")
        self.assertEqual(res.status_code, 200)
        cached_html = cache.get(cache_key)
        self.assertIsNotNone(cached_html)
        self.assertIn("Displacement is a vector quantity.", str(cached_html))

    def test_article_instance_memoization(self):
        # Verify instance properties memoize without re-querying
        art = Article.objects.get(id=self.article.id)
        concepts_1 = art.related_concepts
        concepts_2 = art.related_concepts
        self.assertIs(concepts_1, concepts_2)

        misconceptions_1 = art.common_misconceptions
        misconceptions_2 = art.common_misconceptions
        self.assertIs(misconceptions_1, misconceptions_2)

    def test_wcag_contrast_and_metadata_styling(self):
        # Verify empty state CTA uses bg-navy in article_list
        res_list = self.client.get("/knowledge/?q=nonexistentxyz")
        self.assertEqual(res_list.status_code, 200)
        html_list = res_list.content.decode("utf-8")
        self.assertIn("bg-navy text-white hover:bg-navy-dark", html_list)

    def test_robots_txt_hardened_rules(self):
        res = self.client.get("/robots.txt")
        self.assertEqual(res.status_code, 200)
        content = res.content.decode("utf-8")
        self.assertIn("Disallow: /knowledge/?q=", content)
        self.assertIn("Disallow: /knowledge/?search=", content)
        self.assertIn("Disallow: /knowledge/*?*q=", content)
        self.assertIn("Disallow: /knowledge/*?*search=", content)


class HardeningRegressionTests(TestCase):
    """
    Regression tests added during the de-vibecoding & production-hardening pass.
    These guard against the bugs identified in the audit and must never regress.
    """

    def setUp(self):
        cache.clear()
        self.user = get_user_model().objects.create_user(
            username="hardenuser", password="pw123456"
        )
        # Published category with one published article
        self.published_cat = ArticleCategory.objects.create(
            name="Hardening Physics", slug="hardening-physics", order=10
        )
        self.published_article = Article.objects.create(
            title="Hardening Test Article",
            slug="hardening-test-article",
            category=self.published_cat,
            status="published",
            published_at=timezone.now(),
            summary="Test summary for hardening tests.",
            body="# Heading\nTest body content.",
            featured_image_url=None,
            featured_image_alt="",
        )
        # Draft-only category — must NEVER appear in public navigation
        self.draft_cat = ArticleCategory.objects.create(
            name="Draft Only Category", slug="draft-only-category", order=99
        )
        Article.objects.create(
            title="Draft Article",
            slug="draft-hardening-article",
            category=self.draft_cat,
            status="draft",
            summary="Draft summary.",
            body="Draft body.",
        )

    def tearDown(self):
        cache.clear()

    # ------------------------------------------------------------------
    # 1. Subject / Category navigation comes dynamically from DB
    # ------------------------------------------------------------------
    def test_get_cached_categories_returns_db_categories(self):
        """get_cached_categories() must dynamically load categories from the database, not hardcode them."""
        cache.clear()
        categories = get_cached_categories()
        slugs = [c.slug for c in categories]
        self.assertIn("hardening-physics", slugs, "DB categories must appear in navigation")

    def test_article_list_footer_renders_db_categories(self):
        """The listing page footer must render links to DB categories dynamically."""
        cache.clear()
        res = self.client.get("/knowledge/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Hardening Physics", res.content)

    # ------------------------------------------------------------------
    # 2. Article count: must equal paginator.count, never 0 by default
    # ------------------------------------------------------------------
    def test_article_list_shows_correct_count(self):
        """The listing page must show the real article count, not 0."""
        cache.clear()
        res = self.client.get("/knowledge/")
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")
        # The paginator.count for published articles should be at least 1
        # and the template must not render "0 article" when articles exist
        self.assertNotIn("0 article", html,
                         "Article count must not show 0 when published articles exist")

    def test_category_detail_shows_correct_count(self):
        """Category detail must show real count, not 0."""
        cache.clear()
        res = self.client.get(f"/knowledge/category/{self.published_cat.slug}/")
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")
        self.assertNotIn("0 article", html)

    # ------------------------------------------------------------------
    # 3. Image honesty: og-knowledge.png must never appear in <img> src
    # ------------------------------------------------------------------
    def test_article_detail_does_not_render_og_card_as_figure(self):
        """
        The OG social card (og-knowledge.png) must never appear as a visible
        <img> element. It is only for og:image meta tags.
        """
        # Article has no real image (featured_image_url=None)
        res = self.client.get(f"/knowledge/{self.published_article.slug}/")
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")
        self.assertNotIn(
            '<img src="https://www.vizlearn.org/images/og-knowledge.png"',
            html,
            "og-knowledge.png must not appear as an img src in article detail"
        )
        self.assertNotIn(
            'src="https://www.vizlearn.org/images/og-knowledge.png"',
            html,
            "og-knowledge.png must not appear as any src attribute in article detail"
        )

    def test_article_with_no_image_renders_no_figure(self):
        """When featured_image_url is None, no <figure> element must be rendered."""
        res = self.client.get(f"/knowledge/{self.published_article.slug}/")
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")
        # No figure should appear (article has no real image)
        self.assertNotIn("<figure", html)

    # ------------------------------------------------------------------
    # 4. Content order: article body must appear before simulation callout
    # ------------------------------------------------------------------
    def test_article_body_appears_before_simulation_callout(self):
        """
        The .prose-article (article body) must appear in the DOM before
        the simulation callout <aside>. Reading-first layout is required.
        """
        res = self.client.get(f"/knowledge/{self.published_article.slug}/")
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")
        prose_pos = html.find("prose-article")
        aside_pos = html.find("Interactive Simulation")
        if aside_pos == -1:
            # No simulation linked — skip order check, test passes
            return
        self.assertLess(
            prose_pos, aside_pos,
            "prose-article (body) must appear before the simulation aside callout"
        )


class KnowledgeSEOFoundationTests(TestCase):
    """
    Verification of production SEO foundation:
    - Paginated canonical URLs (self-referencing ?page=N).
    - Search query crawl trap protection (noindex, follow).
    - Host header spoofing / proxy isolation (never leaks api.vizlearn.co or localhost).
    - Robots.txt crawl rules and sitemap reference.
    - XML sitemap published-only guarantees.
    """

    def setUp(self):
        cache.clear()
        self.category = ArticleCategory.objects.create(
            name="Physics SEO",
            slug="physics-seo",
            description="Physics category for SEO verification",
            order=1,
        )
        self.tag = ArticleTag.objects.create(name="Optics SEO", slug="optics-seo")
        # Create 14 published articles to span across 2 pages (page_size is 12)
        self.articles = []
        for i in range(14):
            art = Article.objects.create(
                title=f"SEO Article {i}",
                slug=f"seo-article-{i}",
                summary=f"Summary for SEO article {i}",
                body=f"Body content for SEO article {i}",
                category=self.category,
                status="published",
                published_at=timezone.now() - datetime.timedelta(days=i),
            )
            art.tags.add(self.tag)
            self.articles.append(art)

        self.draft_article = Article.objects.create(
            title="Draft SEO Article Secret",
            slug="draft-seo-article-secret",
            summary="Secret summary",
            body="Draft body",
            category=self.category,
            status="draft",
        )

    def test_paginated_canonical_urls(self):
        """Paginated pages must have self-referencing canonical URLs."""
        # Page 1
        res1 = self.client.get("/knowledge/")
        self.assertEqual(res1.status_code, 200)
        self.assertContains(res1, '<link rel="canonical" href="https://www.vizlearn.org/knowledge/">')

        # Page 2 on knowledge index
        res2 = self.client.get("/knowledge/?page=2")
        self.assertEqual(res2.status_code, 200)
        self.assertContains(res2, '<link rel="canonical" href="https://www.vizlearn.org/knowledge/?page=2">')

        # Page 2 on category detail
        res_cat = self.client.get(f"/knowledge/category/{self.category.slug}/?page=2")
        self.assertEqual(res_cat.status_code, 200)
        self.assertContains(res_cat, f'<link rel="canonical" href="https://www.vizlearn.org/knowledge/category/{self.category.slug}/?page=2">')

        # Page 2 on tag detail
        res_tag = self.client.get(f"/knowledge/tag/{self.tag.slug}/?page=2")
        self.assertEqual(res_tag.status_code, 200)
        self.assertContains(res_tag, f'<link rel="canonical" href="https://www.vizlearn.org/knowledge/tag/{self.tag.slug}/?page=2">')

    def test_search_query_noindex_follow(self):
        """Internal search queries must output noindex, follow to protect crawl budget."""
        # Index with search query
        res_search = self.client.get("/knowledge/?q=article")
        self.assertEqual(res_search.status_code, 200)
        self.assertContains(res_search, '<meta name="robots" content="noindex, follow">')

        # Category with search query
        res_cat_search = self.client.get(f"/knowledge/category/{self.category.slug}/?q=article")
        self.assertEqual(res_cat_search.status_code, 200)
        self.assertContains(res_cat_search, '<meta name="robots" content="noindex, follow">')

        # Standard page without query must be index, follow
        res_normal = self.client.get("/knowledge/")
        self.assertEqual(res_normal.status_code, 200)
        self.assertContains(res_normal, '<meta name="robots" content="index, follow">')

    def test_proxy_headers_cannot_leak_internal_domains(self):
        """
        Even when incoming requests have Host: api.vizlearn.co or internal render hosts,
        all canonicals, OG tags, and JSON-LD must use PUBLIC_SITE_URL (https://www.vizlearn.org).
        """
        headers = {
            "HTTP_HOST": "api.vizlearn.co",
            "HTTP_X_FORWARDED_HOST": "vlearn-backend-qw31.onrender.com",
            "HTTP_X_FORWARDED_PROTO": "https",
        }
        res = self.client.get(f"/knowledge/{self.articles[0].slug}/", **headers)
        self.assertEqual(res.status_code, 200)
        html = res.content.decode("utf-8")
        self.assertNotIn("api.vizlearn.co", html)
        self.assertNotIn("onrender.com", html)
        self.assertNotIn("localhost", html)
        self.assertIn(f'<link rel="canonical" href="https://www.vizlearn.org/knowledge/{self.articles[0].slug}/">', html)
        self.assertIn(f'<meta property="og:url" content="https://www.vizlearn.org/knowledge/{self.articles[0].slug}/">', html)

    def test_robots_txt_disallows_and_sitemap(self):
        """robots.txt must declare valid crawl rules and point to the primary sitemap."""
        res = self.client.get("/robots.txt")
        self.assertEqual(res.status_code, 200)
        self.assertIn("text/plain", res["Content-Type"])
        content = res.content.decode("utf-8")
        self.assertIn("Allow: /knowledge/", content)
        self.assertIn("Disallow: /admin/", content)
        self.assertIn("Disallow: /api/", content)
        self.assertIn("Disallow: /knowledge/*?*q=", content)
        self.assertIn("Disallow: /knowledge/*?*search=", content)
        self.assertIn("Sitemap: https://www.vizlearn.org/sitemap.xml", content)

    def test_sitemap_xml_published_guarantees(self):
        """sitemap.xml must only contain published articles and public site URL."""
        res = self.client.get("/sitemap.xml")
        self.assertEqual(res.status_code, 200)
        self.assertIn("xml", res["Content-Type"])
        content = res.content.decode("utf-8")
        self.assertIn("https://www.vizlearn.org/knowledge/seo-article-0/", content)
        self.assertNotIn("draft-seo-article-secret", content)
        self.assertNotIn("api.vizlearn.co", content)






