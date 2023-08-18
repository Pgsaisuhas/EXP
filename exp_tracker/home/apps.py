# * Import the necessary module for configuring app settings.
from django.apps import AppConfig

class HomeConfig(AppConfig):
    # * Configuration class for the 'home' app.
    
    # * Set the default type for automatically generated primary keys in models.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # ? Name of the app as it appears in Django's app registry.
    name = 'home'

    def ready(self):
        # * This method is executed when the app is ready to be used.
        # * Import and handle signals related to member functionality.
        # ? These signals enable communication and synchronization between different app components.
        import members.signals