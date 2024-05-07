# Import necessary modules from Django
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Define a signal receiver function to create a profile when a new user is saved
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Check if a new user instance is created
    if created:
        # Create a corresponding profile for the new user
        Profile.objects.create(user=instance)

# Define a signal receiver function to save the profile when a user is updated
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Save the profile associated with the user
    instance.profile.save()
