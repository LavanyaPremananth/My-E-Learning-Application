# Import necessary modules from Django
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView
from . import views as user_views

# Define URL patterns for user-related views
urlpatterns = [
    # URL pattern for user registration, mapped to SignUpView
    path('register/', SignUpView.as_view(), name='register'),
    # URL pattern for user login, using Django's built-in LoginView
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # URL pattern for user logout, using Django's built-in LogoutView
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # URL pattern for user profile view, mapped to user_views.profile function
    path('profile/', user_views.profile, name='profile'),
]
