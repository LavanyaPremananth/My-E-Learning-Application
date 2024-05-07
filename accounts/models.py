# Import necessary modules from Django
from django.db import models
from django.contrib.auth.models import User

# Define the Profile model for user profiles
class Profile(models.Model):
    # Define a one-to-one relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # Define an ImageField to store profile pictures, with default and upload directory settings
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        # Return a string representation of the profile, consisting of the user's username and 'Profile' label
        return f'{self.user.username} Profile'
