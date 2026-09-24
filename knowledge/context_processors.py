from django.conf import settings


def analytics_context(request):
    """
    Exposes GA4 Measurement ID and Public Site URL to all templates.
    """
    return {
        "GA4_MEASUREMENT_ID": getattr(settings, "GA4_MEASUREMENT_ID", ""),
        "public_site_url": getattr(settings, "PUBLIC_SITE_URL", "https://www.vizlearn.org").rstrip("/"),
    }
