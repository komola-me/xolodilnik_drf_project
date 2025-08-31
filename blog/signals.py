from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from blog.models import BlogPost, PostCategory, Tag

@receiver(pre_save, sender=BlogPost)
def blog_post_pre_save_handler(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)


@receiver(pre_save, sender=PostCategory)
def post_category_pre_save_handler(sender, instance, **kwargs):
    if instance.name:
        instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Tag)
def tag_pre_save_handler(sender, instance, **kwargs):
    if instance.name:
        instance.slug = slugify(instance.name)