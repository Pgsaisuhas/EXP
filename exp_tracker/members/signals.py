from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import Profile

# * Signal Receiver Function for Creating User Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function that creates a user profile when a new User instance is created.
    
    Args:
        sender (Type): The class of the model sending the signal (User in this case).
        instance (User): The instance of the User model that was just created.
        created (bool): Indicates whether the User instance was just created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        # ? If a new User instance was just created, create a corresponding Profile instance.
        Profile.objects.create(user=instance)
