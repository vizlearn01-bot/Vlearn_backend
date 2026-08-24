"""Entity synchronization logic and foreign key remapping for curriculum publishing."""

import copy
import logging
from django.apps import apps
from django.db import models

from curriculum.publisher.identity import (
    compute_content_hash,
    NATURAL_KEY_MODELS,
    OPERATIONAL_FIELDS,
)

logger = logging.getLogger(__name__)


class FKRemapper:
    """Tracks and resolves local database primary keys to target database primary keys."""

    def __init__(self, source_db: str = 'default', target_db: str = 'publish_target'):
        self.source_db = source_db
        self.target_db = target_db
        # Map of (model_name, local_pk) -> target_pk
        self._pk_map: dict[tuple[str, int], int] = {}
        # Pre-loaded syncers registry
        self._syncers: dict[str, 'BaseEntitySyncer'] = {}

    def register_syncer(self, model_name: str, syncer: 'BaseEntitySyncer'):
        self._syncers[model_name] = syncer

    def register(self, model_name: str, local_pk: int, target_pk: int):
        self._pk_map[(model_name, local_pk)] = target_pk

    def get(self, model_name: str, local_pk: int) -> int | None:
        return self._pk_map.get((model_name, local_pk))

    def resolve_fk(self, target_model_class, local_fk_id: int | None) -> int | None:
        if local_fk_id is None:
            return None

        model_name = target_model_class.__name__
        cached = self.get(model_name, local_fk_id)
        if cached is not None:
            return cached

        # Look up source object from source DB
        try:
            source_obj = target_model_class.objects.using(self.source_db).get(pk=local_fk_id)
        except target_model_class.DoesNotExist:
            logger.warning(f"Source object {model_name} with PK {local_fk_id} not found in source DB.")
            return None

        # Find matching target object via cached syncer
        syncer = self._syncers.get(model_name)
        if syncer is None:
            syncer = get_syncer_for_model(model_name, self.source_db, self.target_db)
            self._syncers[model_name] = syncer

        target_match = syncer.match(source_obj)
        if target_match:
            self.register(model_name, local_fk_id, target_match.pk)
            return target_match.pk

        return None


class BaseEntitySyncer:
    """Base class for model-level synchronization with in-memory caching, clean PK generation, and batched writes."""

    def __init__(self, model_name: str, source_db: str = 'default', target_db: str = 'publish_target'):
        self.model_name = model_name
        self.source_db = source_db
        self.target_db = target_db
        self.model_class = apps.get_model('curriculum', model_name)
        self._target_cache_by_uuid: dict = {}
        self._target_cache_by_natural_key: dict = {}
        self._target_cache_loaded = False

    def get_source_queryset(self, scope_filters: dict | None = None):
        qs = self.model_class.objects.using(self.source_db).all()
        if scope_filters:
            qs = qs.filter(**scope_filters)
        return qs

    def get_target_queryset(self):
        return self.model_class.objects.using(self.target_db).all()

    def load_target_cache(self):
        if self._target_cache_loaded:
            return
        qs = self.get_target_queryset()
        if self.model_name in ('Grade', 'Subject'):
            qs = qs.select_related('grade__curriculum' if self.model_name == 'Subject' else 'curriculum')
        elif self.model_name in NATURAL_KEY_MODELS:
            pass
        else:
            qs = qs.only('id', 'content_uuid', 'content_hash')

        for obj in qs:
            if hasattr(obj, 'content_uuid') and obj.content_uuid:
                self._target_cache_by_uuid[obj.content_uuid] = obj
            if self.model_name in NATURAL_KEY_MODELS:
                key = self._get_natural_key_tuple(obj)
                if key:
                    self._target_cache_by_natural_key[key] = obj
        self._target_cache_loaded = True

    def _get_natural_key_tuple(self, obj) -> tuple | None:
        if self.model_name == 'Curriculum':
            return (obj.name,)
        elif self.model_name == 'Grade':
            curr_name = obj.curriculum.name if obj.curriculum_id and hasattr(obj, 'curriculum') else None
            return (curr_name, obj.name)
        elif self.model_name == 'Subject':
            grade = obj.grade if obj.grade_id and hasattr(obj, 'grade') else None
            curr_name = grade.curriculum.name if grade and grade.curriculum_id and hasattr(grade, 'curriculum') else None
            grade_name = grade.name if grade else None
            return (curr_name, grade_name, obj.name)
        elif self.model_name == 'Simulation':
            return (obj.key,)
        return None

    def match(self, source_obj) -> models.Model | None:
        self.load_target_cache()
        if self.model_name in NATURAL_KEY_MODELS:
            key = self._get_natural_key_tuple(source_obj)
            return self._target_cache_by_natural_key.get(key)
        else:
            if hasattr(source_obj, 'content_uuid') and source_obj.content_uuid:
                return self._target_cache_by_uuid.get(source_obj.content_uuid)
            return None

    def has_changed(self, source_obj, target_obj) -> bool:
        source_hash = getattr(source_obj, 'content_hash', None)
        target_hash = getattr(target_obj, 'content_hash', None)
        if source_hash and target_hash:
            return source_hash != target_hash
        if not source_hash:
            source_hash = compute_content_hash(source_obj)
        if not target_hash:
            target_hash = compute_content_hash(target_obj)
        return source_hash != target_hash

    def prepare_field_values(self, source_obj, fk_remapper: FKRemapper) -> dict:
        """Prepares field values for creating or updating a target record.

        CRITICAL: Never includes primary key / AutoField (id/pk) in the returned dict.
        All foreign keys are dynamically resolved to their corresponding target PKs.
        """
        values = {}
        concrete_fields = [f for f in self.model_class._meta.concrete_fields if not f.primary_key]

        exclude_fields = {'created_at', 'updated_at', 'id', 'pk'}
        if self.model_name in OPERATIONAL_FIELDS:
            exclude_fields.update(OPERATIONAL_FIELDS[self.model_name])

        for field in concrete_fields:
            if field.name in exclude_fields:
                continue

            if field.is_relation and field.many_to_one:
                # Foreign key field: resolve local FK to target FK
                local_fk_id = getattr(source_obj, field.attname)
                if local_fk_id is None:
                    values[field.attname] = None
                else:
                    related_model = field.related_model
                    target_fk_id = fk_remapper.resolve_fk(related_model, local_fk_id)
                    if target_fk_id is None and not field.null:
                        raise ValueError(
                            f"Cannot resolve required FK '{field.name}' on {self.model_name} (source ID {source_obj.pk}) "
                            f"pointing to {related_model.__name__} (source ID {local_fk_id}). "
                            f"Ensure parent records are published before child records."
                        )
                    values[field.attname] = target_fk_id
            else:
                val = getattr(source_obj, field.attname)
                # Deep copy for JSON/dict/list fields to prevent mutation
                if isinstance(val, (dict, list)):
                    val = copy.deepcopy(val)
                values[field.attname] = val

        # Ensure content_hash is set
        if 'content_hash' in [f.name for f in concrete_fields]:
            values['content_hash'] = source_obj.content_hash or compute_content_hash(source_obj)

        return values

    def create(self, source_obj, fk_remapper: FKRemapper, dry_run: bool = False) -> models.Model:
        """Creates a single record in the target database with a fresh target-generated primary key."""
        field_values = self.prepare_field_values(source_obj, fk_remapper)
        target_obj = self.model_class(**field_values)
        target_obj.pk = None
        if hasattr(target_obj, 'id'):
            target_obj.id = None

        if hasattr(source_obj, 'content_uuid') and source_obj.content_uuid:
            target_obj.content_uuid = source_obj.content_uuid

        if not dry_run:
            target_obj.save(using=self.target_db)
            fk_remapper.register(self.model_name, source_obj.pk, target_obj.pk)
            if hasattr(target_obj, 'content_uuid') and target_obj.content_uuid:
                self._target_cache_by_uuid[target_obj.content_uuid] = target_obj
            if self.model_name in NATURAL_KEY_MODELS:
                key = self._get_natural_key_tuple(target_obj)
                if key:
                    self._target_cache_by_natural_key[key] = target_obj
        else:
            fk_remapper.register(self.model_name, source_obj.pk, source_obj.pk)

        return target_obj

    def update(self, source_obj, target_obj, fk_remapper: FKRemapper, dry_run: bool = False) -> models.Model:
        """Updates an existing target record in place."""
        field_values = self.prepare_field_values(source_obj, fk_remapper)
        for field_name, value in field_values.items():
            setattr(target_obj, field_name, value)

        if not dry_run:
            target_obj.save(using=self.target_db)

        fk_remapper.register(self.model_name, source_obj.pk, target_obj.pk)
        return target_obj

    def sync_batch(self, source_objects: list, fk_remapper: FKRemapper, dry_run: bool = False):
        """High-performance batch synchronization.

        Groups records into unchanged, to_create, and to_update.
        Inserts new records using bulk_create (batch_size=500) and maps the newly generated
        PostgreSQL primary keys back to fk_remapper in seconds.
        """
        self.load_target_cache()

        to_create_src = []
        to_create_tgt = []
        to_update_pairs = []

        for src in source_objects:
            match = self.match(src)
            if match is None:
                field_values = self.prepare_field_values(src, fk_remapper)
                tgt = self.model_class(**field_values)
                tgt.pk = None
                if hasattr(tgt, 'id'):
                    tgt.id = None
                if hasattr(src, 'content_uuid') and src.content_uuid:
                    tgt.content_uuid = src.content_uuid
                to_create_src.append(src)
                to_create_tgt.append(tgt)
            else:
                if self.has_changed(src, match):
                    to_update_pairs.append((src, match))
                else:
                    fk_remapper.register(self.model_name, src.pk, match.pk)

        if not dry_run:
            # Batch creates
            if to_create_tgt:
                created_objs = self.model_class.objects.using(self.target_db).bulk_create(
                    to_create_tgt, batch_size=500
                )
                for src, tgt in zip(to_create_src, created_objs):
                    fk_remapper.register(self.model_name, src.pk, tgt.pk)
                    if hasattr(tgt, 'content_uuid') and tgt.content_uuid:
                        self._target_cache_by_uuid[tgt.content_uuid] = tgt
                    if self.model_name in NATURAL_KEY_MODELS:
                        key = self._get_natural_key_tuple(tgt)
                        if key:
                            self._target_cache_by_natural_key[key] = tgt

            # Updates (if any)
            if to_update_pairs:
                update_fields = set()
                updated_tgts = []
                for src, tgt in to_update_pairs:
                    field_values = self.prepare_field_values(src, fk_remapper)
                    for field_name, value in field_values.items():
                        setattr(tgt, field_name, value)
                        update_fields.add(field_name)
                    updated_tgts.append(tgt)
                    fk_remapper.register(self.model_name, src.pk, tgt.pk)
                if update_fields:
                    self.model_class.objects.using(self.target_db).bulk_update(
                        updated_tgts, list(update_fields), batch_size=500
                    )
        else:
            for src in to_create_src:
                fk_remapper.register(self.model_name, src.pk, src.pk)
            for src, tgt in to_update_pairs:
                fk_remapper.register(self.model_name, src.pk, tgt.pk)

    def sync_m2m(self, source_obj, target_obj, fk_remapper: FKRemapper, dry_run: bool = False):
        """Sync ManyToMany relationships if any (single object fallback)."""
        pass

    def sync_m2m_batch(self, source_objects: list, fk_remapper: FKRemapper, dry_run: bool = False):
        """Sync ManyToMany relationships in bulk (high-performance batch)."""
        pass


class LessonAssetSyncer(BaseEntitySyncer):
    """LessonAsset syncer that also handles M2M relationship to LessonBlocks in bulk."""

    def __init__(self, source_db: str = 'default', target_db: str = 'publish_target'):
        super().__init__('LessonAsset', source_db, target_db)

    def sync_m2m(self, source_obj, target_obj, fk_remapper: FKRemapper, dry_run: bool = False):
        if dry_run:
            return
        fk_remapper.register('LessonAsset', source_obj.pk, target_obj.pk)
        self.sync_m2m_batch([source_obj], fk_remapper, dry_run=False)

    def sync_m2m_batch(self, source_objects: list, fk_remapper: FKRemapper, dry_run: bool = False):
        if dry_run or not source_objects:
            return

        from curriculum.models import LessonAsset
        ThroughModel = LessonAsset.blocks.through

        source_asset_ids = [s.pk for s in source_objects]
        source_throughs = ThroughModel.objects.using(self.source_db).filter(
            lessonasset_id__in=source_asset_ids
        )

        target_through_instances = []
        for st in source_throughs:
            target_asset_id = fk_remapper.get('LessonAsset', st.lessonasset_id)
            target_block_id = fk_remapper.get('LessonBlock', st.lessonblock_id)
            if target_asset_id and target_block_id:
                target_through_instances.append(
                    ThroughModel(lessonasset_id=target_asset_id, lessonblock_id=target_block_id)
                )

        if target_through_instances:
            ThroughModel.objects.using(self.target_db).bulk_create(
                target_through_instances, batch_size=500, ignore_conflicts=True
            )


def get_syncer_for_model(model_name: str, source_db: str = 'default', target_db: str = 'publish_target') -> BaseEntitySyncer:
    """Factory to get the appropriate syncer for a model."""
    if model_name == 'LessonAsset':
        return LessonAssetSyncer(source_db, target_db)
    else:
        return BaseEntitySyncer(model_name, source_db, target_db)
