from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if kwargs.get('raw', False):
        return
    if created:
        # Create UserProfile if it doesn't exist 
        # when a new user signs up it creates a user model for them to update their profile afterwards with additional information about themselves
        UserProfile.objects.get_or_create(user=instance)
