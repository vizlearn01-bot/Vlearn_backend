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


urlpatterns = [
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
    path("", include("Resources.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
