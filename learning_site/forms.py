# Import necessary modules
from django import forms
from django.core import validators

# Define custom validator function
def must_be_empty(value):
    # If the value is not empty, raise a validation error
    if value:
        raise forms.ValidationError('is not empty')

# Define the SuggestionForm class, which inherits from Django's Form class
class SuggestionForm(forms.Form):
    # Define form fields
    name = forms.CharField()
    email = forms.EmailField()
    # Email field for verification with help text
    verify_email = forms.EmailField(help_text="Please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    # Hidden field to catch spam bots with custom validator
    honeypot = forms.CharField(
        required=False,  # Field not required
        widget=forms.HiddenInput,  # Hidden input widget
        label="Leave empty",  # Label for honeypot field
        validators=[must_be_empty]  # Apply custom validator
    )

    # Define a clean method to perform additional validation
    def clean(self):
        # Cleaned form data
        cleaned_data = super().clean()
        # Get cleaned email and verified email from cleaned data
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        # Check if the entered email and verified email are identical
        if email != verify:
            # If not identical, raise a validation error
            raise forms.ValidationError("You need to enter the same email in both fields")
