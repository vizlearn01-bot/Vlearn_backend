from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_generationjob_knowledgepack_lesson_knowledge_pack_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generationrule',
            name='is_mandatory',
            field=models.BooleanField(
                default=False,
                help_text='If True, this block must be present for a lesson to be published',
            ),
        ),
    ]
