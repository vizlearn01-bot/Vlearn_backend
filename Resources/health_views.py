from django.http import JsonResponse
from django.db import connection
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def health_check(request):
    """
    Liveness probe: Returns 200 OK as long as the Django application process is running.
    """
    return JsonResponse({
        "status": "healthy",
        "service": "vlearn-backend"
    }, status=200)


def readiness_check(request):
    """
    Readiness probe: Checks database connectivity and optional Redis cache/broker reachability.
    Returns 200 OK if critical dependencies are reachable, otherwise 503.
    """
    checks = {
        "database": "unknown",
        "redis": "unknown",
    }
    is_ready = True

    # 1. Database check
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            cursor.fetchone()
        checks["database"] = "connected"
    except Exception as e:
        logger.error(f"Readiness check database failure: {e}")
        checks["database"] = f"unhealthy: {str(e)}"
        is_ready = False

    # 2. Redis check (if configured)
    broker_url = getattr(settings, "CELERY_BROKER_URL", None)
    if broker_url and broker_url.startswith("redis"):
        try:
            import redis
            r = redis.from_url(broker_url, socket_connect_timeout=2)
            r.ping()
            checks["redis"] = "connected"
        except Exception as e:
            logger.warning(f"Readiness check redis warning: {e}")
            checks["redis"] = f"unreachable: {str(e)}"
            # Redis failure is non-fatal for primary HTTP readiness if DB is healthy,
            # but logged in checks dict.
    else:
        checks["redis"] = "not_configured"

    status_code = 200 if is_ready else 503
    response_data = {
        "status": "ready" if is_ready else "not_ready",
        "checks": checks
    }
    return JsonResponse(response_data, status=status_code)
