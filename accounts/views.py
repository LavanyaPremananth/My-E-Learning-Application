# Import necessary modules from Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm

# Define views for user-related functionality

# View for user registration
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')   # Redirect to login page after successful registration
    template_name = 'users/register.html'

# View for user profile, requiring login
@login_required
def profile(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # If POST, initialize user and profile update forms with request data and current user instance
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # Check if both forms are valid
        if u_form.is_valid() and p_form.is_valid():
            # Save updated user and profile information
            u_form.save()
            p_form.save()
            # Display success message
            messages.success(request, f'Your profile has been updated!')
            # Redirect to the profile page
            return redirect('profile')

    else:
        # If request method is not POST, initialize forms with current user instance
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Prepare context to pass to the template
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    # Render the profile template with the context
    return render(request, 'users/profile.html', context)
