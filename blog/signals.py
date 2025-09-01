from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify

from blog.models import BlogPost, PostCategory, Tag
from blog.choices import PostStatus

@receiver(pre_save, sender=BlogPost)
def blog_post_pre_save_handler(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)
    if instance.status == PostStatus.PUBLISHED and not instance.published_at:
        instance.published_at = instance.created_at
    elif instance.status == PostStatus.DRAFT:
        instance.published_at = None


@receiver(post_delete, sender=BlogPost)
def delete_related_files(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=PostCategory)
def post_category_pre_save_handler(sender, instance, **kwargs):
    if instance.name:
        instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Tag)
def tag_pre_save_handler(sender, instance, **kwargs):
    if instance.name:
        instance.slug = slugify(instance.name)