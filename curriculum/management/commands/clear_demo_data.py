from django.core.management.base import BaseCommand
from curriculum.models import Curriculum, Grade, Subject, Topic, Lesson, KnowledgePack, LearningUnit

class Command(BaseCommand):
    help = 'Clears all demonstration curriculum data to provide a clean slate.'

    def handle(self, *args, **kwargs):
        # Delete everything
        KnowledgePack.objects.all().delete()
        Lesson.objects.all().delete()
        LearningUnit.objects.all().delete()
        Topic.objects.all().delete()
        Subject.objects.all().delete()
        Grade.objects.all().delete()
        Curriculum.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Successfully cleared all curriculum data.'))
