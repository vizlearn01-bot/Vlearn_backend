"""
URL configuration for Nexus_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView


from Resources.health_views import health_check, readiness_check
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from knowledge.sitemaps import sitemaps
from knowledge.views import RobotsTxtView


import sys

def sitemap_view(request, **kwargs):
    if "test" in sys.argv or getattr(settings, "TESTING", False):
        return sitemap(request, **kwargs)
    return cache_page(60 * 60 * 12, key_prefix="sitemap")(sitemap)(request, **kwargs)


import os
from django.http import FileResponse, Http404

def serve_knowledge_image(request, filename="vlearn_icon.png"):
    safe_name = os.path.basename(filename)
    file_path = os.path.join(settings.BASE_DIR, "knowledge", "static", "images", safe_name)
    if os.path.exists(file_path):
        content_type = "image/png" if safe_name.endswith(".png") else "image/svg+xml"
        response = FileResponse(open(file_path, "rb"), content_type=content_type)
        response["Cache-Control"] = "public, max-age=86400"
        return response
    raise Http404

urlpatterns = [
    path("favicon.ico", lambda r: serve_knowledge_image(r, "vlearn_icon.png"), name="favicon"),
    path("images/<str:filename>", serve_knowledge_image),
    path("static/images/<str:filename>", serve_knowledge_image),
    path("admin/", admin.site.urls),
    path("health/", health_check, name="health_check"),
    path("ready/", readiness_check, name="readiness_check"),
    path("api/health/", health_check, name="api_health_check"),
    path("api/ready/", readiness_check, name="api_readiness_check"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/subscriptions/", include("subscriptions.api.urls")),
    path("api/billing-and-payments/", include("billing_payment.api.urls")),
    path("api/curriculum/", include("curriculum.api.urls")),
    path("api/organizations/", include("organizations.urls")),
    path("api/assessments/", include("assessments.urls")),
    path("api/performance/", include("assessments.urls")),
    path("questions/", include("Questions.urls")),
    path("api/auth/", include("Resources.auth_urls")),
    path("api/knowledge/", include("knowledge.api.urls")),
    path("knowledge/", include("knowledge.urls")),
    path("sitemap.xml", sitemap_view, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", RobotsTxtView.as_view(), name="robots_txt"),
    path("", include("Resources.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
