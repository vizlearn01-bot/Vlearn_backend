import os
import dj_database_url
from django.conf import settings
from django.db import connections

class PublishConnection:
    """Manages the production database connection lifecycle."""
    ALIAS = 'publish_target'
    
    def __init__(self):
        self.target_config = None
        self.source_config = settings.DATABASES['default']
    
    def configure(self) -> dict:
        """Parse PUBLISH_DATABASE_URL and return config dict."""
        db_url = os.environ.get('PUBLISH_DATABASE_URL')
        if not db_url:
            raise ValueError("PUBLISH_DATABASE_URL environment variable is not set")
        self.target_config = dj_database_url.parse(db_url)
        self.target_config.setdefault('OPTIONS', {})
        self.target_config.setdefault('ATOMIC_REQUESTS', False)
        self.target_config.setdefault('AUTOCOMMIT', True)
        self.target_config.setdefault('TIME_ZONE', None)
        self.target_config.setdefault('TEST', {})
        return self.target_config
    
    def validate_source_target_differ(self):
        """Raise if source == target database."""
        if not self.target_config or not self.source_config:
            return
            
        target_host = self.target_config.get('HOST', '')
        target_db = self.target_config.get('NAME', '')
        source_host = self.source_config.get('HOST', '')
        source_db = self.source_config.get('NAME', '')
        
        if target_host == source_host and target_db == source_db:
            raise ValueError("Target database and source database are the same. Publishing aborted.")
    
    def get_target_display(self) -> str:
        """Return safe display string for target (no credentials)."""
        if not self.target_config:
            return "Not configured"
        return f"{self.target_config.get('HOST', 'localhost')}:{self.target_config.get('NAME', '')}"
    
    def get_source_display(self) -> str:
        """Return safe display string for source (no credentials)."""
        if not self.source_config:
            return "Not configured"
        return f"{self.source_config.get('HOST', 'localhost')}:{self.source_config.get('NAME', '')}"
    
    def connect(self):
        """Register the target database connection with Django."""
        self.configure()
        self.validate_source_target_differ()
        settings.DATABASES[self.ALIAS] = self.target_config
        connections.databases[self.ALIAS] = self.target_config

    def disconnect(self):
        """Clean up the target database connection."""
        if self.ALIAS in connections:
            connections[self.ALIAS].close()
        if self.ALIAS in connections.databases:
            del connections.databases[self.ALIAS]
        if self.ALIAS in settings.DATABASES:
            del settings.DATABASES[self.ALIAS]
    
    def __enter__(self):
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
