"""
WSGI config for learning_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

# Import necessary modules
import os
from django.core.wsgi import get_wsgi_application

# Set default value for DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_site.settings')

# Get WSGI application for the Django project
application = get_wsgi_application()
