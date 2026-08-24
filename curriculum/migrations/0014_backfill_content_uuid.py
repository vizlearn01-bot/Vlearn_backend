import hashlib
import json
import uuid
from django.db import migrations, models

VLEARN_NAMESPACE = uuid.UUID('a1b2c3d4-e5f6-7890-abcd-ef1234567890')

UUID_MODELS = [
    'PedagogyTemplate',
    'GenerationRule',
    'Topic',
    'LearningUnit',
    'Lesson',
    'LessonBlock',
    'LessonAsset',
    'KnowledgePack',
    'KnowledgeChunk',
    'Concept',
    'ConceptRelationship',
    'LearningObjective',
    'Misconception',
    'LearningExperienceGraph',
]

HASH_MODELS = [
    'Curriculum',
    'Grade',
    'Subject',
    'Simulation',
] + UUID_MODELS


def backfill_uuids_and_hashes(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    for model_name in HASH_MODELS:
        Model = apps.get_model('curriculum', model_name)
        has_uuid = model_name in UUID_MODELS
        
        objects = list(Model.objects.using(db_alias).all())
        if not objects:
            continue

        for obj in objects:
            if has_uuid:
                obj.content_uuid = uuid.uuid5(VLEARN_NAMESPACE, f"{model_name}:{obj.pk}")

            # Compute content hash
            fields = [f for f in obj._meta.fields if f.name not in (
                'id', 'pk', 'created_at', 'updated_at', 'content_uuid', 'content_hash', 'immutable_metadata'
            )]
            fields.sort(key=lambda f: f.name)
            parts = []
            for f in fields:
                val = getattr(obj, f.attname, None)
                if val is None:
                    parts.append(f"{f.name}:null")
                elif isinstance(val, (dict, list)):
                    try:
                        parts.append(f"{f.name}:{json.dumps(val, sort_keys=True)}")
                    except Exception:
                        parts.append(f"{f.name}:{str(val)}")
                else:
                    parts.append(f"{f.name}:{str(val)}")
            obj.content_hash = hashlib.sha256("|".join(parts).encode('utf-8')).hexdigest()

        update_fields = ['content_uuid', 'content_hash'] if has_uuid else ['content_hash']
        Model.objects.using(db_alias).bulk_update(objects, update_fields, batch_size=2000)


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0013_add_content_uuid_and_hash'),
    ]

    operations = [
        migrations.RunPython(backfill_uuids_and_hashes, reverse_code=migrations.RunPython.noop),
        # Make content_uuid unique across all 14 models
        migrations.AlterField(
            model_name='pedagogytemplate',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='generationrule',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='learningunit',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='lessonblock',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='lessonasset',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='knowledgepack',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='knowledgechunk',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='concept',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='conceptrelationship',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='learningobjective',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='misconception',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
        migrations.AlterField(
            model_name='learningexperiencegraph',
            name='content_uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Stable cross-database identity for curriculum publishing.', unique=True),
        ),
    ]
