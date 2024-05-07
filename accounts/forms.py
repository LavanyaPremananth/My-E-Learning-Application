# Import necessary modules from Django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Define a custom form for user registration
class SignUpForm(UserCreationForm):
    # Define additional fields for first name, last name, and email
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        # Set the model to User and specify fields to include in the form
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
        ]


# Define a form for updating user information
class UserUpdateForm(forms.ModelForm):
    # Define an additional field for email
    email = forms.EmailField()

    class Meta:
        # Set the model to User and specify fields to include in the form
        model = User
        fields = ['username', 'email']


# Define a form for updating profile information
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        # Set the model to Profile and specify fields to include in the form
        model = Profile
        fields = ['image']
