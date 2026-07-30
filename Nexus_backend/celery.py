import os
from celery import Celery
from django.utils import timezone

# Set default Django settings module for 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')

app = Celery('Nexus_backend')

# Load task modules from all registered Django app configs
# Namespace 'CELERY' means all celery-related config keys must be prefixed with 'CELERY_'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed Django apps
app.autodiscover_tasks()


@app.task(name='Nexus_backend.ping_celery', bind=True)
def ping_celery(self):
    """
    Phase 1 Infrastructure Health-Check Task.
    Verifies that Django can enqueue, Redis accepts, and Celery worker executes messages.
    """
    return {
        "status": "pong",
        "task_id": self.request.id,
        "timestamp": timezone.now().isoformat(),
    }
