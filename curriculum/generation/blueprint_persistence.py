"""
curriculum/generation/blueprint_persistence.py

Persists a translated blueprint (list of block-kwargs dicts produced by
SkeletonTranslator.translate()) into the database.

Responsibilities
----------------
- Delete any existing blocks for the lesson (full re-generation path).
- Create LessonBlock rows using the existing persistence layer where possible.
- For every block whose _asset_instruction is set, create a *pending*
  LessonAsset slot so that the Content Studio immediately shows the
  administrator exactly what media the AI requests.
- Return a summary dict for the caller.

This module does NOT call the LLM.
It does NOT modify the prompt.
It does NOT touch the legacy V1 orchestrator.
"""

from __future__ import annotations
from typing import Any

from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.generation.skeleton import SUGGESTED_TO_ASSET_TYPE


# Map from _asset_type string to a LessonAsset.asset_type choice.
# skeleton.py already defines SUGGESTED_TO_ASSET_TYPE, but the LessonAsset
# model uses a slightly different vocabulary for some keys.
_ASSET_TYPE_MAP: dict[str, str] = {
    'diagram':       'diagram',
    'video':         'video',
    'image':         'image',
    'simulation':    'simulation',
    'gif':           'gif',
    'external_link': 'external_link',
    'activity':      'external_link',   # activities stored as external_link
    'repository_asset': 'image',        # fallback; admin will override
}


class BlueprintPersistenceService:
    """
    Saves a fully-translated blueprint into LessonBlocks and LessonAssets.
    """

    @staticmethod
    def save_blueprint(lesson: Lesson, block_kwargs_list: list[dict[str, Any]]) -> dict:
        """
        Persist the blueprint output for *lesson*.

        - Deletes all existing blocks for the lesson (full replacement).
        - Creates one LessonBlock per entry in block_kwargs_list.
        - Creates one pending LessonAsset for every block that carries an
          _asset_instruction value.

        Returns
        -------
        dict
            {'blocks_created': int, 'assets_created': int}
        """
        # ── Wipe previous content for this lesson ─────────────────────────────
        lesson.blocks.all().delete()
        lesson.assets.all().delete()

        blocks_created = 0
        assets_created = 0

        for kwargs in block_kwargs_list:
            # ── Extract private blueprint keys ─────────────────────────────────
            asset_instruction: str | None = kwargs.pop('_asset_instruction', None)
            asset_type_key: str | None    = kwargs.pop('_asset_type', None)

            # ── Create the LessonBlock ─────────────────────────────────────────
            block = LessonBlock.objects.create(
                lesson=lesson,
                block_type=kwargs['block_type'],
                title=kwargs.get('title', ''),
                content=kwargs.get('content', {}),
                order=kwargs['order'],
                # V2 presentation fields (null for legacy blocks)
                page_number=kwargs.get('page_number'),
                page_title=kwargs.get('page_title'),
                component_type=kwargs.get('component_type'),
                component_order=kwargs.get('component_order'),
            )
            blocks_created += 1

            # ── Create a pending LessonAsset slot for suggested components ─────
            if asset_instruction and asset_type_key:
                resolved_asset_type = _ASSET_TYPE_MAP.get(asset_type_key, 'image')

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type=resolved_asset_type,
                    source_type='uploaded',    # admin will provide the media
                    storage_type='url',
                    status='pending',
                    title=block.title or block.block_type.replace('_', ' ').title(),
                    description=asset_instruction,
                    metadata={'ai_instruction': asset_instruction},
                )
                asset.blocks.add(block)
                assets_created += 1

        return {'blocks_created': blocks_created, 'assets_created': assets_created}
