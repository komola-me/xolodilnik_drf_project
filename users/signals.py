from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import User

@receiver(pre_save, sender=User)
def user_pre_save_handler(sender, instance, **kwargs):
    if not instance.username:
        username_text = f"{instance.first_name}-{instance.last_name}"
        if username_text:
            instance.username = slugify(username_text)
        else:
            username_short = instance.email[:5]
            instance.username = slugify(username_short)