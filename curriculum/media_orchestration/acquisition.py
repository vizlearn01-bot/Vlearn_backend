import logging
from typing import List, Dict
from .contracts import MediaManifest, MediaRequirement, ResolvedAsset
from .search_intelligence.query_builder import QueryBuilder
from .search_intelligence.ranking import AssetRankingEngine
from .providers.registry import ProviderRegistry

logger = logging.getLogger("curriculum.generation")


class MediaAcquisitionEngine:
    """
    Module 2: Media Acquisition Engine (Deterministic).
    Iterates through MediaManifest, builds search payloads, queries the Provider Registry,
    and returns ranked retrieved assets.

    Processes both required and optional media requirements.
    Tracks acquisition telemetry per node for compiler trace.
    """

    def __init__(self):
        self.registry = ProviderRegistry()
        self.query_builder = QueryBuilder()
        self.ranking_engine = AssetRankingEngine()
        self._cache: Dict[str, List[ResolvedAsset]] = {}

    def resolve_manifest(self, manifest: MediaManifest) -> List[ResolvedAsset]:
        resolved_assets = []
        skipped = 0
        not_found = 0

        from .providers.youtube import YouTubeProvider

        for req in manifest.requirements:
            # Build deterministic search payload
            payload = self.query_builder.build_payload(req)
            is_video_req = (req.preferred_media_type == 'video' or 'video' in (req.media_category or '').lower())

            # Skip if Wikimedia is not suitable AND requirement is optional (only applies to non-video requests)
            if not is_video_req and not payload.is_suitable_for_wikimedia and not req.is_required:
                skipped += 1
                continue

            cache_key = f"acq_{payload.primary_query}_{payload.preferred_media_category}"
            if cache_key in self._cache:
                for asset in self._cache[cache_key]:
                    copied_asset = asset.model_copy(deep=True)
                    copied_asset.node_id = req.node_id
                    resolved_assets.append(copied_asset)
                continue

            candidates = []
            if is_video_req:
                # Video requirement: query YouTube provider directly first
                yt_provider = next((p for p in self.registry.get_providers() if isinstance(p, YouTubeProvider)), None)
                if yt_provider:
                    try:
                        candidates.extend(yt_provider.search(payload, req.node_id))
                    except Exception as e:
                        logger.warning("[ACQUISITION] YouTubeProvider failed for node '%s': %s", req.node_id, e)

                # If YouTube did not find an asset, fallback to other providers
                if not candidates:
                    for provider in self.registry.get_providers():
                        if not isinstance(provider, YouTubeProvider):
                            try:
                                candidates.extend(provider.search(payload, req.node_id))
                            except Exception:
                                pass
            else:
                for provider in self.registry.get_providers():
                    # For non-video requirements, skip YouTubeProvider
                    if isinstance(provider, YouTubeProvider):
                        continue
                    try:
                        provider_assets = provider.search(payload, req.node_id)
                        candidates.extend(provider_assets)
                    except Exception as e:
                        logger.warning("[ACQUISITION] Provider %s failed for node '%s': %s",
                                       type(provider).__name__, req.node_id, e)

            ranked_candidates = self.ranking_engine.rank_assets(candidates, preferred_type=req.preferred_media_type)

            # Select top 1 asset per node (quality over quantity)
            top_assets = ranked_candidates[:1]

            if top_assets:
                self._cache[cache_key] = top_assets
                resolved_assets.extend(top_assets)
            else:
                not_found += 1
                if req.is_required:
                    logger.warning(
                        "[ACQUISITION] No asset found for required node '%s' (query='%s').",
                        req.node_id, payload.primary_query
                    )

        logger.info(
            "[ACQUISITION] Resolved %d assets | skipped=%d | not_found=%d | total_requirements=%d",
            len(resolved_assets), skipped, not_found, len(manifest.requirements)
        )

        return resolved_assets
