# Import necessary modules
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# Define URL patterns
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    # Include URLs from the 'courses' app
    path('courses/', include('courses.urls')),
    # Include URLs from the 'accounts' app
    path('', include('accounts.urls')),
    # URL pattern for suggestion view
    path('suggest/', views.suggestion_view, name='suggestion'),
    # Default URL pattern for home view
    path('', views.home, name='home'),
    path('chat/', include('chat.urls', namespace='chat')),
]

# Serve static files during development
urlpatterns += staticfiles_urlpatterns()

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
