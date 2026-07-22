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

        for req in manifest.requirements:
            # Build deterministic search payload
            payload = self.query_builder.build_payload(req)

            # Skip if Wikimedia is not suitable AND requirement is optional
            if not payload.is_suitable_for_wikimedia and not req.is_required:
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
            for provider in self.registry.get_providers():
                try:
                    provider_assets = provider.search(payload, req.node_id)
                    candidates.extend(provider_assets)
                except Exception as e:
                    logger.warning("[ACQUISITION] Provider %s failed for node '%s': %s",
                                   type(provider).__name__, req.node_id, e)

            ranked_candidates = self.ranking_engine.rank_assets(candidates)

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
