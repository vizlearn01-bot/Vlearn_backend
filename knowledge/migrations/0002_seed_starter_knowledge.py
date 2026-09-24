from django.db import migrations
from django.core.management import call_command


def seed_knowledge_articles(apps, schema_editor):
    call_command("seed_starter_knowledge")


def reverse_seed_knowledge_articles(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("knowledge", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            seed_knowledge_articles,
            reverse_code=reverse_seed_knowledge_articles,
        ),
    ]
