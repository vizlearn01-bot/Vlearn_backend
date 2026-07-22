import re
import requests
from typing import List, Optional
from django.core.cache import cache
from curriculum.media_orchestration.contracts import ResolvedAsset
from curriculum.media_orchestration.search_intelligence.models import SearchPayload
from .base import BaseProvider

# Titles containing these substrings are likely decorative/irrelevant
_SKIP_TITLE_PATTERNS = re.compile(
    r'\b(logo|icon|symbol|flag|coat.of.arms|emblem|badge|seal|favicon|avatar|'
    r'stamp|sticker|placeholder|blank|template|button)\b',
    re.IGNORECASE
)

# Minimum acceptable image dimensions
_MIN_WIDTH = 200
_MIN_HEIGHT = 200


class WikimediaProvider(BaseProvider):
    @property
    def provider_name(self) -> str:
        return "Wikimedia Commons"

    def __init__(self):
        self.api_url = "https://commons.wikimedia.org/w/api.php"
        self.session = requests.Session()

    def search(self, payload: SearchPayload, node_id: str) -> List[ResolvedAsset]:
        if not payload.is_suitable_for_wikimedia:
            return []

        # Try all queries in order: primary first, then layered fallbacks
        queries_to_try = [payload.primary_query] + payload.alternate_queries

        for query in queries_to_try:
            if not query or len(query.strip()) < 2:
                continue

            assets = self._execute_search(query, node_id)
            if assets:
                return assets

        return []

    def _execute_search(self, query: str, node_id: str) -> List[ResolvedAsset]:
        cache_key = f"wikimedia_search_{query.lower().replace(' ', '_')[:60]}"
        cached_assets = cache.get(cache_key)

        if cached_assets is not None:
            # Duplicate assets with updated node_id for this requester
            result = []
            for asset in cached_assets:
                a = asset.model_copy(deep=True)
                a.node_id = node_id
                result.append(a)
            return result

        params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": f"filetype:bitmap|drawing|svg {query}",
            "gsrnamespace": 6,  # File namespace
            "gsrlimit": 10,     # Wider candidate pool (was 5)
            "prop": "imageinfo",
            "iiprop": "url|extmetadata|dimensions"
        }

        try:
            response = self.session.get(self.api_url, params=params, timeout=8.0)  # was 5.0
            response.raise_for_status()
            data = response.json()
        except Exception:
            return []

        pages = data.get("query", {}).get("pages", {})
        assets = []

        for page_id, page_data in pages.items():
            imageinfo = page_data.get("imageinfo", [])
            if not imageinfo:
                continue

            info = imageinfo[0]
            extmetadata = info.get("extmetadata", {})

            title = page_data.get("title", "").replace("File:", "").strip()
            url = info.get("url")
            width = info.get("width", 0)
            height = info.get("height", 0)

            if not url:
                continue

            # Quality filter: skip tiny images
            if isinstance(width, (int, float)) and isinstance(height, (int, float)):
                if width < _MIN_WIDTH or height < _MIN_HEIGHT:
                    continue

            # Quality filter: skip decorative/irrelevant titles
            if _SKIP_TITLE_PATTERNS.search(title):
                continue

            license_val = extmetadata.get("LicenseShortName", {}).get("value", "Unknown")
            author_html = extmetadata.get("Artist", {}).get("value", "Unknown Author")
            attribution = extmetadata.get("Credit", {}).get("value", "")
            description = extmetadata.get("ImageDescription", {}).get("value", title)

            asset = ResolvedAsset(
                node_id=node_id,
                asset_type="image",
                url=url,
                provenance="Wikimedia Commons",
                source="Wikimedia Commons",
                provider=self.provider_name,
                licensing=license_val,
                alt_text=title,
                confidence_score=0.8,
                verified=False,
                author=self._strip_html(author_html),
                attribution=self._strip_html(attribution),
                metadata={
                    "width": width,
                    "height": height,
                    "description": self._strip_html(description),
                    "search_query": query,
                }
            )
            assets.append(asset)

        if assets:
            cache.set(cache_key, assets, timeout=86400)  # 24 hours

        return assets

    def _strip_html(self, text: str) -> str:
        """Simple HTML stripper for metadata fields."""
        if not text:
            return ""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text).strip()
