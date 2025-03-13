from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Resources'
    
    def ready(self):
        # Import signals to ensure they are registered when the app starts
        import Resources.signals