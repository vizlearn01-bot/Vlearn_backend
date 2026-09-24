import json
import bleach
import markdown
from django.conf import settings
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.http import HttpResponse
from django.utils.html import mark_safe
from django.views import generic, View

from knowledge.models import Article, ArticleCategory, ArticleTag
from curriculum.models import Concept, ConceptRelationship, LearningUnit


ALLOWED_TAGS = [
    "h2",
    "h3",
    "h4",
    "h5",
    "p",
    "ul",
    "ol",
    "li",
    "strong",
    "em",
    "code",
    "pre",
    "blockquote",
    "a",
    "img",
    "table",
    "thead",
    "tbody",
    "tr",
    "th",
    "td",
    "br",
    "span",
    "hr",
]

ALLOWED_ATTRIBUTES = {
    "a": ["href", "title", "target", "rel"],
    "img": ["src", "alt", "title", "loading", "class"],
    "code": ["class"],
    "span": ["class"],
    "th": ["align"],
    "td": ["align"],
    "h2": ["id"],
    "h3": ["id"],
    "h4": ["id"],
    "h5": ["id"],
}

ALLOWED_PROTOCOLS = ["http", "https", "mailto"]


def link_filter(attrs, new=False):
    """
    Enforces rel="noopener noreferrer" on target="_blank" and outbound external http/https links.
    Internal links on vizlearn domains are not modified unless target="_blank".
    """
    href = attrs.get((None, "href"), "")
    target = attrs.get((None, "target"), "")
    is_external = False
    if href.startswith("http://") or href.startswith("https://"):
        if not ("vizlearn.org" in href or "vizlearn.co" in href):
            is_external = True

    if target == "_blank" or is_external:
        existing_rel = attrs.get((None, "rel"), "")
        rel_tokens = set(existing_rel.split()) if existing_rel else set()
        rel_tokens.update(["noopener", "noreferrer"])
        attrs[(None, "rel")] = " ".join(sorted(rel_tokens))
    return attrs


def render_article_markdown(content: str) -> str:
    """
    Renders raw Markdown content to secure, sanitized HTML using markdown extensions,
    bleach sanitization, and rel="noopener noreferrer" link security.
    """
    if not content:
        return mark_safe("")

    raw_html = markdown.markdown(
        content,
        extensions=["tables", "fenced_code", "toc"],
    )
    clean_html = bleach.clean(
        raw_html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        protocols=ALLOWED_PROTOCOLS,
        strip=True,
    )
    linkified_html = bleach.linkify(
        clean_html,
        callbacks=[link_filter],
        skip_tags=["pre", "code"],
    )
    return mark_safe(linkified_html)


def get_cached_categories():
    """
    Returns all ArticleCategory items cached for 1 hour.
    """
    return cache.get_or_set(
        "knowledge_all_categories",
        lambda: list(ArticleCategory.objects.all().order_by("order", "name")),
        timeout=3600,
    )


def get_cached_popular_tags():
    """
    Returns top 12 active tags on published articles cached for 1 hour.
    """
    return cache.get_or_set(
        "knowledge_popular_tags",
        lambda: list(
            ArticleTag.objects.filter(articles__status="published")
            .distinct()[:12]
        ),
        timeout=3600,
    )


class ArticleListView(generic.ListView):
    """
    Public paginated list of published knowledge articles with search and category filtering.
    """
    model = Article
    template_name = "knowledge/article_list.html"
    context_object_name = "articles"
    paginate_by = 12

    def get_queryset(self):
        qs = (
            Article.objects.filter(status="published")
            .select_related("category")
            .order_by("-published_at")
        )
        category_slug = self.request.GET.get("category")
        if category_slug:
            qs = qs.filter(category__slug=category_slug)

        tag_slug = self.request.GET.get("tag")
        if tag_slug:
            qs = qs.filter(tags__slug=tag_slug)

        search_query = self.request.GET.get("q") or self.request.GET.get("search")
        if search_query and search_query.strip():
            from knowledge.search import search_articles
            qs = search_articles(qs, search_query.strip())

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        public_site_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/")
        page_obj = context.get("page_obj")
        if page_obj and page_obj.number > 1:
            canonical_url = f"{public_site_url}/knowledge/?page={page_obj.number}"
        else:
            canonical_url = f"{public_site_url}/knowledge/"
        context["canonical_url"] = canonical_url
        context["public_site_url"] = public_site_url

        categories = get_cached_categories()
        context["categories"] = categories
        context["popular_tags"] = get_cached_popular_tags()
        category_slug = self.request.GET.get("category")
        context["current_category"] = (
            next((c for c in categories if c.slug == category_slug), None)
            if category_slug
            else None
        )
        tag_slug = self.request.GET.get("tag")
        context["current_tag"] = (
            ArticleTag.objects.filter(slug=tag_slug).first()
            if tag_slug
            else None
        )
        search_query = self.request.GET.get("q") or self.request.GET.get("search")
        context["search_query"] = search_query.strip() if search_query else ""

        # Structured Data: Schema.org Graph for Knowledge Index
        articles = context.get("articles", [])
        item_list = [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "url": f"{public_site_url}/knowledge/{art.slug}/",
                "name": art.title,
            }
            for idx, art in enumerate(articles)
        ]

        schema_graph = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "EducationalOrganization",
                    "@id": f"{public_site_url}/#organization",
                    "name": "VizLearn",
                    "url": public_site_url,
                    "logo": {
                        "@type": "ImageObject",
                        "url": f"{public_site_url}/images/logo.png",
                    },
                    "description": "Visual, interactive STEM learning platform for secondary school education.",
                    "sameAs": ["https://twitter.com/VizLearn01"],
                },
                {
                    "@type": "WebSite",
                    "@id": f"{public_site_url}/#website",
                    "url": public_site_url,
                    "name": "VizLearn",
                    "potentialAction": {
                        "@type": "SearchAction",
                        "target": f"{public_site_url}/knowledge/?q={{search_term_string}}",
                        "query-input": "required name=search_term_string",
                    },
                },
                {
                    "@type": "CollectionPage",
                    "@id": f"{canonical_url}#collection",
                    "url": canonical_url,
                    "name": "VizLearn Knowledge Base — Visual STEM Concepts",
                    "description": "Explore curated STEM articles, simulations, and KCSE-aligned explanations.",
                    "mainEntity": {
                        "@type": "ItemList",
                        "itemListElement": item_list,
                    },
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": f"{canonical_url}#breadcrumbs",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{public_site_url}/"},
                        {"@type": "ListItem", "position": 2, "name": "Knowledge", "item": canonical_url},
                    ],
                },
            ],
        }
        json_str = json.dumps(schema_graph, indent=2).replace("<", "\\u003c").replace(">", "\\u003e")
        context["json_ld"] = mark_safe(json_str)
        return context


class ArticleDetailView(generic.DetailView):
    """
    Public article detail view rendering server-side HTML with rich SEO metadata,
    curriculum context, simulation links, KaTeX math support, and JSON-LD.
    """
    model = Article
    template_name = "knowledge/article_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "article"
    queryset = (
        Article.objects.filter(status="published")
        .select_related(
            "linked_topic__subject__grade__curriculum",
            "linked_learning_unit",
            "linked_simulation",
            "category",
            "author",
        )
        .prefetch_related(
            "tags",
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
                queryset=LearningUnit.objects.prefetch_related(
                    Prefetch(
                        "concepts",
                        queryset=Concept.objects.prefetch_related(
                            "misconceptions",
                            Prefetch(
                                "outgoing_relationships",
                                queryset=ConceptRelationship.objects.select_related("target"),
                            ),
                        ),
                    )
                ),
            ),
            Prefetch(
                "related_articles",
                queryset=Article.objects.filter(status="published").select_related("category"),
                to_attr="published_related_articles",
            ),
        )
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        public_site_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/")

        # Rendered Markdown body with Bleach sanitization and Python cache
        markdown_cache_key = f"article_rendered_markdown_{article.id}_{article.updated_at.timestamp()}"
        context["rendered_body"] = cache.get_or_set(
            markdown_cache_key,
            lambda: render_article_markdown(article.body),
            timeout=86400,
        )

        # In-memory access to prefetched published related articles
        related = getattr(article, "published_related_articles", [])
        if not related:
            fallback_qs = (
                Article.objects.filter(status="published")
                .exclude(pk=article.pk)
                .select_related("category", "author")
                .prefetch_related("tags")
            )
            if article.category:
                related = list(fallback_qs.filter(category=article.category)[:3])
            if not related and article.linked_topic:
                related = list(fallback_qs.filter(linked_topic=article.linked_topic)[:3])
        context["related_articles"] = related[:3]

        # Pedagogical Knowledge Graph: Concepts & Misconceptions
        context["related_concepts"] = article.related_concepts
        context["common_misconceptions"] = article.common_misconceptions

        # Canonical URL bound to PUBLIC_SITE_URL
        canonical_url = f"{public_site_url}/knowledge/{article.slug}/"
        context["canonical_url"] = canonical_url
        context["public_site_url"] = public_site_url

        # Structured Data: Schema.org Graph
        fallback_image = f"{public_site_url}/images/og-knowledge.png"

        # 1. Article Schema
        article_schema = {
            "@type": "Article",
            "@id": f"{canonical_url}#article",
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": canonical_url,
            },
            "headline": article.meta_title or article.title,
            "description": article.meta_description or article.summary,
            "image": [article.featured_image_url] if article.featured_image_url else [fallback_image],
            "datePublished": (
                article.published_at.isoformat()
                if article.published_at
                else article.created_at.isoformat()
            ),
            "dateModified": article.updated_at.isoformat(),
            "inLanguage": "en",
            "publisher": {
                "@type": "EducationalOrganization",
                "@id": f"{public_site_url}/#organization",
                "name": "VizLearn",
                "url": public_site_url,
                "logo": {
                    "@type": "ImageObject",
                    "url": f"{public_site_url}/images/logo.png",
                },
            },
        }

        if article.author:
            author_name = article.author.get_full_name() or article.author.username
            article_schema["author"] = {
                "@type": "Person",
                "name": author_name,
            }
        else:
            article_schema["author"] = {
                "@type": "EducationalOrganization",
                "name": "VizLearn Academic Team",
                "url": public_site_url,
            }

        # 2. Breadcrumbs schema bound to PUBLIC_SITE_URL
        breadcrumbs = [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": f"{public_site_url}/",
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Knowledge",
                "item": f"{public_site_url}/knowledge/",
            },
        ]
        if article.category:
            breadcrumbs.append({
                "@type": "ListItem",
                "position": 3,
                "name": article.category.name,
                "item": f"{public_site_url}/knowledge/category/{article.category.slug}/",
            })
            breadcrumbs.append({
                "@type": "ListItem",
                "position": 4,
                "name": article.title,
                "item": canonical_url,
            })
        else:
            breadcrumbs.append({
                "@type": "ListItem",
                "position": 3,
                "name": article.title,
                "item": canonical_url,
            })

        breadcrumb_schema = {
            "@type": "BreadcrumbList",
            "@id": f"{canonical_url}#breadcrumbs",
            "itemListElement": breadcrumbs,
        }

        # Contextual Simulation & Curriculum Bridge
        context["simulation_teaser"] = article.simulation_teaser
        context["simulation_cta_label"] = article.simulation_cta_label
        context["curriculum_lineage"] = article.curriculum_lineage

        # Categories for shared footer navigation (same as listing views)
        context["categories"] = get_cached_categories()

        schema_elements = [article_schema, breadcrumb_schema]

        # 3. Educational Structured Data: Schema.org LearningResource / EducationalApplication
        if article.linked_simulation:
            sim = article.linked_simulation
            sim_url = f"{public_site_url}/student/simulations?sim={sim.key}"
            learning_resource_schema = {
                "@type": "LearningResource",
                "@id": sim_url,
                "name": sim.title,
                "description": sim.description or article.summary,
                "learningResourceType": "interactive simulation",
                "applicationCategory": "EducationalApplication",
                "url": sim_url,
                "inLanguage": "en",
            }
            if article.curriculum_lineage and article.curriculum_lineage.get("grade"):
                learning_resource_schema["educationalLevel"] = article.curriculum_lineage["grade"]
            if article.linked_topic:
                learning_resource_schema["about"] = article.linked_topic.name

            article_schema["hasPart"] = [
                {
                    "@type": "LearningResource",
                    "@id": sim_url,
                    "name": sim.title,
                }
            ]
            article_schema["potentialAction"] = {
                "@type": "InteractAction",
                "target": sim_url,
                "name": article.simulation_cta_label,
            }
            schema_elements.append(learning_resource_schema)

        # 4. Common Misconceptions: FAQPage / Q&A Schema
        misconceptions = context.get("common_misconceptions", [])
        if misconceptions:
            qa_entities = []
            for misc in misconceptions:
                qa_entities.append({
                    "@type": "Question",
                    "name": f"Common Misconception: {misc.description}",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": misc.correction,
                    },
                })
            faq_schema = {
                "@type": "FAQPage",
                "@id": f"{canonical_url}#misconceptions",
                "isPartOf": {"@id": f"{canonical_url}#article"},
                "mainEntity": qa_entities,
            }
            schema_elements.append(faq_schema)

        schema_graph = {
            "@context": "https://schema.org",
            "@graph": schema_elements,
        }
        json_str = json.dumps(schema_graph, indent=2).replace("<", "\\u003c").replace(">", "\\u003e")
        context["json_ld"] = mark_safe(json_str)

        return context


class CategoryDetailView(generic.DetailView):
    """
    Public category detail view listing published articles in that category.
    """
    model = ArticleCategory
    template_name = "knowledge/category_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        public_site_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/")
        context["public_site_url"] = public_site_url

        articles_qs = (
            Article.objects.filter(category=category, status="published")
            .select_related("category")
            .order_by("-published_at")
        )
        search_query = self.request.GET.get("q") or self.request.GET.get("search")
        context["search_query"] = search_query.strip() if search_query else ""
        if context["search_query"]:
            from knowledge.search import search_articles
            articles_qs = search_articles(articles_qs, context["search_query"])

        paginator = Paginator(articles_qs, 12)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        if page_obj.number > 1:
            canonical_url = f"{public_site_url}/knowledge/category/{category.slug}/?page={page_obj.number}"
        else:
            canonical_url = f"{public_site_url}/knowledge/category/{category.slug}/"
        context["canonical_url"] = canonical_url

        context["articles"] = page_obj
        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        context["categories"] = get_cached_categories()

        # Structured Data: Schema.org Graph for Category Page
        item_list = [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "url": f"{public_site_url}/knowledge/{art.slug}/",
                "name": art.title,
            }
            for idx, art in enumerate(page_obj)
        ]

        schema_graph = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "CollectionPage",
                    "@id": f"{canonical_url}#collection",
                    "url": canonical_url,
                    "name": f"{category.name} Concepts & Articles | VizLearn Knowledge",
                    "description": category.description or f"Explore {category.name} STEM concepts and simulations.",
                    "about": category.name,
                    "mainEntity": {
                        "@type": "ItemList",
                        "itemListElement": item_list,
                    },
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": f"{canonical_url}#breadcrumbs",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{public_site_url}/"},
                        {"@type": "ListItem", "position": 2, "name": "Knowledge", "item": f"{public_site_url}/knowledge/"},
                        {"@type": "ListItem", "position": 3, "name": category.name, "item": canonical_url},
                    ],
                },
            ],
        }
        json_str = json.dumps(schema_graph, indent=2).replace("<", "\\u003c").replace(">", "\\u003e")
        context["json_ld"] = mark_safe(json_str)
        return context


class TagDetailView(generic.DetailView):
    """
    Public tag detail view listing published articles associated with a specific tag.
    """
    model = ArticleTag
    template_name = "knowledge/tag_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "tag"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.object
        public_site_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/")
        context["public_site_url"] = public_site_url

        articles_qs = (
            Article.objects.filter(tags=tag, status="published")
            .select_related("category")
            .order_by("-published_at")
        )
        search_query = self.request.GET.get("q") or self.request.GET.get("search")
        context["search_query"] = search_query.strip() if search_query else ""
        if context["search_query"]:
            from knowledge.search import search_articles
            articles_qs = search_articles(articles_qs, context["search_query"])

        paginator = Paginator(articles_qs, 12)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        if page_obj.number > 1:
            canonical_url = f"{public_site_url}/knowledge/tag/{tag.slug}/?page={page_obj.number}"
        else:
            canonical_url = f"{public_site_url}/knowledge/tag/{tag.slug}/"
        context["canonical_url"] = canonical_url

        context["articles"] = page_obj
        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        context["categories"] = get_cached_categories()
        all_popular = get_cached_popular_tags()
        context["popular_tags"] = [t for t in all_popular if t.id != tag.id][:10]

        # Structured Data: Schema.org Graph for Tag Page
        item_list = [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "url": f"{public_site_url}/knowledge/{art.slug}/",
                "name": art.title,
            }
            for idx, art in enumerate(page_obj)
        ]

        schema_graph = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "CollectionPage",
                    "@id": f"{canonical_url}#collection",
                    "url": canonical_url,
                    "name": f"#{tag.name} Articles & Explanations | VizLearn Knowledge",
                    "about": tag.name,
                    "mainEntity": {
                        "@type": "ItemList",
                        "itemListElement": item_list,
                    },
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": f"{canonical_url}#breadcrumbs",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{public_site_url}/"},
                        {"@type": "ListItem", "position": 2, "name": "Knowledge", "item": f"{public_site_url}/knowledge/"},
                        {"@type": "ListItem", "position": 3, "name": f"#{tag.name}", "item": canonical_url},
                    ],
                },
            ],
        }
        json_str = json.dumps(schema_graph, indent=2).replace("<", "\\u003c").replace(">", "\\u003e")
        context["json_ld"] = mark_safe(json_str)
        return context


class RobotsTxtView(View):
    """
    Serves plain text robots.txt file for search engine spiders.
    Guards crawl budget by preventing indexing of internal search query loops
    and private authenticated SPA routes.
    """
    def get(self, request, *args, **kwargs):
        public_site_url = getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/")
        lines = [
            "User-agent: *",
            "Allow: /knowledge/",
            "Allow: /static/",
            "Disallow: /admin/",
            "Disallow: /api/",
            "Disallow: /knowledge/*?*q=",
            "Disallow: /knowledge/*?*search=",
            "Disallow: /knowledge/?q=",
            "Disallow: /knowledge/?search=",
            "Disallow: /student/",
            "Disallow: /teacher/",
            "Disallow: /school/",
            "Disallow: /admin-dashboard/",
            "Disallow: /reset-password/",
            "Disallow: /invitation/",
            f"Sitemap: {public_site_url}/sitemap.xml",
        ]
        return HttpResponse("\n".join(lines) + "\n", content_type="text/plain; charset=utf-8")
