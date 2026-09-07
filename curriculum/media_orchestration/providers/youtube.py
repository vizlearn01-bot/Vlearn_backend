import logging
import re
import urllib.request
import urllib.parse
import json
from typing import List, Optional
from django.core.cache import cache
from curriculum.media_orchestration.contracts import ResolvedAsset
from curriculum.media_orchestration.search_intelligence.models import SearchPayload
from .base import BaseProvider

logger = logging.getLogger("curriculum.generation")


class YouTubeProvider(BaseProvider):
    @property
    def provider_name(self) -> str:
        return "YouTube"

    def search(self, payload: SearchPayload, node_id: str) -> List[ResolvedAsset]:
        # If the payload indicates a video requirement or the query looks for an explanation/experiment/video
        queries_to_try = [payload.primary_query] + payload.alternate_queries

        for raw_query in queries_to_try:
            if not raw_query or len(raw_query.strip()) < 2:
                continue

            query = raw_query.strip()
            # If query is a direct YouTube URL or video ID, resolve directly
            direct_id = self._extract_video_id(query)
            if direct_id:
                asset = self.resolve_video_id(direct_id, node_id)
                if asset:
                    return [asset]

            if not any(k in query.lower() for k in ['experiment', 'explanation', 'animation', 'lesson', 'concept', 'physics', 'chemistry', 'biology', 'math', 'aviation', 'video']):
                search_term = f"{query} educational explanation video"
            else:
                search_term = query

            assets = self._execute_search(search_term, node_id)
            if assets:
                return assets

        return []

    def _execute_search(self, query: str, node_id: str) -> List[ResolvedAsset]:
        cache_key = f"yt_search_{urllib.parse.quote(query.lower())[:60]}"
        cached = cache.get(cache_key)
        if cached:
            results = []
            for item in cached:
                copied = item.model_copy(deep=True)
                copied.node_id = node_id
                results.append(copied)
            return results

        try:
            search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
            req = urllib.request.Request(
                search_url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            )
            with urllib.request.urlopen(req, timeout=6) as response:
                html = response.read().decode('utf-8', errors='ignore')

            video_ids = re.findall(r'\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
            seen = set()
            unique_ids = [vid for vid in video_ids if not (vid in seen or seen.add(vid))]

            assets = []
            for vid in unique_ids[:5]:
                meta = self.validate_video(vid)
                if meta:
                    video_url = f"https://www.youtube.com/watch?v={vid}"
                    title = meta.get('title', f"Educational Video for {query}")
                    author = meta.get('author_name', 'YouTube Creator')
                    asset = ResolvedAsset(
                        node_id=node_id,
                        asset_type='video',
                        url=video_url,
                        provenance='YouTube',
                        licensing='Standard YouTube License',
                        alt_text=f"{title} by {author}",
                        confidence_score=0.95,
                        source='YouTube',
                        provider=self.provider_name,
                        author=author,
                        attribution=f"YouTube / {author}",
                        metadata={
                            'video_id': vid,
                            'title': title,
                            'author_name': author,
                            'youtube_url': video_url,
                            'embed_url': f"https://www.youtube.com/embed/{vid}"
                        }
                    )
                    assets.append(asset)
                    if len(assets) >= 1:
                        break

            if assets:
                cache.set(cache_key, assets, timeout=86400 * 7)
            return assets

        except Exception as e:
            logger.warning("[YOUTUBE PROVIDER] Search failed for '%s': %s", query, e)
            return []

    @classmethod
    def _extract_video_id(cls, text: str) -> Optional[str]:
        if not text:
            return None
        m = re.search(r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})', text)
        if m:
            return m.group(1)
        if re.fullmatch(r'[a-zA-Z0-9_-]{11}', text.strip()):
            return text.strip()
        return None

    @classmethod
    def validate_video(cls, video_id: str) -> Optional[dict]:
        """Validates video via oEmbed API to verify it exists and is public."""
        if not video_id or len(video_id) != 11:
            return None
        cache_key = f"yt_valid_{video_id}"
        cached = cache.get(cache_key)
        if cached is not None:
            return cached or None

        oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
        try:
            req = urllib.request.Request(oembed_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=4) as response:
                meta = json.loads(response.read().decode('utf-8'))
                cache.set(cache_key, meta, timeout=86400 * 14)
                return meta
        except Exception:
            cache.set(cache_key, False, timeout=86400 * 7)
            return None

    @classmethod
    def resolve_video_id(cls, video_id: str, node_id: str, fallback_query: str = "") -> Optional[ResolvedAsset]:
        """Resolves and validates a video ID directly, returning a verified ResolvedAsset."""
        meta = cls.validate_video(video_id)
        if not meta:
            return None
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        title = meta.get('title', f"Educational Video {video_id}")
        author = meta.get('author_name', 'YouTube Creator')
        return ResolvedAsset(
            node_id=node_id,
            asset_type='video',
            url=video_url,
            provenance='YouTube',
            licensing='Standard YouTube License',
            alt_text=f"{title} by {author}",
            confidence_score=0.98,
            source='YouTube',
            provider='YouTube',
            author=author,
            attribution=f"YouTube / {author}",
            metadata={
                'video_id': video_id,
                'title': title,
                'author_name': author,
                'youtube_url': video_url,
                'embed_url': f"https://www.youtube.com/embed/{video_id}"
            }
        )
