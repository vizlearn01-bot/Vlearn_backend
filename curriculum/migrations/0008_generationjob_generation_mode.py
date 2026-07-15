# Generated manually – adds generation_mode to GenerationJob
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0007_lessonblock_v2_fields_and_lesson_asset'),
    ]

    operations = [
        migrations.AddField(
            model_name='generationjob',
            name='generation_mode',
            field=models.CharField(
                max_length=20,
                choices=[
                    ('legacy',    'Legacy (V1 block-by-block)'),
                    ('blueprint', 'Instructional Blueprint (V2)'),
                ],
                default='legacy',
                help_text=(
                    "Controls which generation engine is used. "
                    "'legacy' preserves the V1 GenerationRule loop; "
                    "'blueprint' uses the Instructional Designer AI."
                ),
            ),
        ),
    ]
