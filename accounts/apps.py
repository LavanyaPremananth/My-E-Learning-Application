# Import the AppConfig class from the django.apps module
from django.apps import AppConfig

# Define a custom configuration for the 'accounts' app
class AccountsConfig(AppConfig):
    # Set the name attribute to 'accounts' to identify the app
    name = 'accounts'

    # Define a method called ready(), which is executed when the app is ready
    def ready(self):
        # Import the signals module from the 'accounts' app package
        import accounts.signals
