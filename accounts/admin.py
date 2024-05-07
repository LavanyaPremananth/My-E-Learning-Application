# Import the admin module from Django.contrib package
from django.contrib import admin

# Import the Profile model from the current directory's models file
from .models import Profile

# Register the Profile model with the Django admin interface
admin.site.register(Profile)
