# Import necessary modules
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .import forms

# Define view for the home page
def home(request):
    return render(request, 'home.html')

# Define view for suggestion form
def suggestion_view(request):
    # Initialize suggestion form
    form = forms.SuggestionForm()

    # If request method is POST, process form data
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        # If form is valid, send email and show success message
        if form.is_valid():
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']),  # Subject
                form.cleaned_data['suggestion'],  # Body
                '{name} <{email}>'.format(**form.cleaned_data),  # From email
                ['utkarsh21@gmail.com'],  # Sent To
            )
            messages.add_message(request, messages.SUCCESS, 'Thanks For Your Suggestion!')
            return HttpResponseRedirect(reverse('suggestion'))

    # Render suggestion form template with form
    return render(request, 'suggestion_form.html', {'form': form})
