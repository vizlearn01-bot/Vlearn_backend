"""Media classification, validation, and upload handler for curriculum publishing."""

import os
import urllib.parse
from dataclasses import dataclass, field
from django.conf import settings
from django.core.files.storage import default_storage

try:
    import cloudinary
    import cloudinary.uploader
    CLOUDINARY_AVAILABLE = True
except ImportError:
    CLOUDINARY_AVAILABLE = False


@dataclass
class MediaItem:
    model_name: str
    object_id: int
    field_name: str
    value: str
    media_type: str  # 'external_url', 'cloudinary', 'local_file', 'missing_file'
    resolved_url: str = ''
    error: str = ''


@dataclass
class MediaAuditReport:
    items: list[MediaItem] = field(default_factory=list)
    
    @property
    def external_count(self) -> int:
        return sum(1 for item in self.items if item.media_type == 'external_url')
        
    @property
    def cloudinary_count(self) -> int:
        return sum(1 for item in self.items if item.media_type == 'cloudinary')
        
    @property
    def local_file_count(self) -> int:
        return sum(1 for item in self.items if item.media_type == 'local_file')
        
    @property
    def missing_file_count(self) -> int:
        return sum(1 for item in self.items if item.media_type == 'missing_file')
        
    @property
    def has_missing_files(self) -> bool:
        return self.missing_file_count > 0
        
    def get_missing_summary(self) -> list[str]:
        return [
            f"{item.model_name} (ID {item.object_id}).{item.field_name}: '{item.value}' — {item.error}"
            for item in self.items if item.media_type == 'missing_file'
        ]


class MediaAuditor:
    """Audits all media references in curriculum content within the scope."""
    
    def __init__(self, source_db: str = 'default'):
        self.source_db = source_db
        
    def audit_scope(self, lessons=None, knowledge_packs=None) -> MediaAuditReport:
        report = MediaAuditReport()
        
        # 1. Audit LessonAssets
        from curriculum.models import LessonAsset
        assets_qs = LessonAsset.objects.using(self.source_db).all()
        if lessons is not None:
            assets_qs = assets_qs.filter(lesson__in=lessons)
            
        for asset in assets_qs:
            # Check url field
            if asset.url:
                item = self._classify_url('LessonAsset', asset.pk, 'url', asset.url)
                report.items.append(item)
            # Check file field
            if asset.file:
                item = self._classify_file('LessonAsset', asset.pk, 'file', asset.file)
                report.items.append(item)
                
        # 2. Audit KnowledgeChunks
        from curriculum.models import KnowledgeChunk
        chunks_qs = KnowledgeChunk.objects.using(self.source_db).exclude(image='').exclude(image__isnull=True)
        if knowledge_packs is not None:
            chunks_qs = chunks_qs.filter(knowledge_pack__in=knowledge_packs)
            
        for chunk in chunks_qs:
            if chunk.image:
                item = self._classify_file('KnowledgeChunk', chunk.pk, 'image', chunk.image)
                report.items.append(item)
                
        # 3. Audit KnowledgePacks
        from curriculum.models import KnowledgePack
        kp_qs = KnowledgePack.objects.using(self.source_db).all()
        if knowledge_packs is not None:
            kp_qs = kp_qs.filter(pk__in=[kp.pk for kp in knowledge_packs])
            
        for kp in kp_qs:
            if kp.source_file_url:
                item = self._classify_url('KnowledgePack', kp.pk, 'source_file_url', kp.source_file_url)
                report.items.append(item)
            if kp.file:
                item = self._classify_file('KnowledgePack', kp.pk, 'file', kp.file)
                report.items.append(item)
                
        return report

    def _classify_url(self, model_name: str, object_id: int, field_name: str, url: str) -> MediaItem:
        if not url:
            return MediaItem(model_name, object_id, field_name, '', 'missing_file', error="Empty URL")
            
        url_lower = url.lower()
        if 'res.cloudinary.com' in url_lower or 'cloudinary' in url_lower:
            return MediaItem(model_name, object_id, field_name, url, 'cloudinary', resolved_url=url)
        elif url_lower.startswith('http://') or url_lower.startswith('https://') or url_lower.startswith('simulation://') or url_lower.startswith('vlearn://'):
            return MediaItem(model_name, object_id, field_name, url, 'external_url', resolved_url=url)
        else:
            return MediaItem(model_name, object_id, field_name, url, 'missing_file', error=f"Invalid URL format: {url}")

    def _classify_file(self, model_name: str, object_id: int, field_name: str, file_field) -> MediaItem:
        file_name = str(file_field)
        if not file_name:
            return MediaItem(model_name, object_id, field_name, '', 'missing_file', error="Empty file reference")
            
        # If it contains a Cloudinary URL or Cloudinary path
        if 'res.cloudinary.com' in file_name or file_name.startswith('http://') or file_name.startswith('https://'):
            return MediaItem(model_name, object_id, field_name, file_name, 'cloudinary', resolved_url=file_name)
            
        # Check if file exists locally on disk
        media_root = getattr(settings, 'MEDIA_ROOT', '')
        local_path = os.path.join(media_root, file_name) if media_root else file_name
        
        if os.path.exists(local_path):
            return MediaItem(model_name, object_id, field_name, file_name, 'local_file', resolved_url=local_path)
        elif not os.path.isabs(file_name) and not file_name.startswith('/'):
            # Relative key managed by Cloudinary storage
            return MediaItem(model_name, object_id, field_name, file_name, 'cloudinary', resolved_url=file_name)
        else:
            return MediaItem(
                model_name, object_id, field_name, file_name, 'missing_file',
                error=f"Local file not found on disk at {local_path}"
            )


class MediaPublisher:
    """Handles uploading local files to Cloudinary during publication."""
    
    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run
        if CLOUDINARY_AVAILABLE and not self.dry_run:
            c_storage = getattr(settings, 'CLOUDINARY_STORAGE', {})
            cloudinary.config(
                cloud_name=c_storage.get('CLOUD_NAME') or os.getenv('CLOUDINARY_CLOUD_NAME'),
                api_key=c_storage.get('API_KEY') or os.getenv('CLOUDINARY_API_KEY'),
                api_secret=c_storage.get('API_SECRET') or os.getenv('CLOUDINARY_API_SECRET'),
                secure=True,
            )
        
    def upload_local_file(self, local_path: str, folder: str = "curriculum") -> str:
        """
        Uploads a local file to Cloudinary and returns the secure URL or remote reference.
        """
        if self.dry_run:
            return f"https://res.cloudinary.com/dry-run/{os.path.basename(local_path)}"
            
        if not CLOUDINARY_AVAILABLE:
            raise RuntimeError("Cloudinary SDK is not installed or configured.")
            
        try:
            response = cloudinary.uploader.upload(
                local_path,
                folder=folder,
                resource_type="auto"
            )
            return response.get('secure_url', response.get('url', ''))
        except Exception as e:
            raise RuntimeError(f"Failed to upload {local_path} to Cloudinary: {e}")
