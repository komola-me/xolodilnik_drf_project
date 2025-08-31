from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from .choices import PostStatus

# Create your models here.
class BlogPost(BaseModel):
    title = models.CharField(max_length=250, verbose_name=_("Post Title"))
    slug = models.SlugField(unique_for_date="published_at", verbose_name=_("Slug"))
    content = models.TextField(verbose_name=_("Post Content"))

    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="posts", verbose_name=_("Author"))
    category = models.ForeignKey("blog.PostCategory", on_delete=models.SET_NULL, related_name="posts", null=True, blank=True, verbose_name=_("Post Category"))
    tags = models.ManyToManyField("blog.Tag", related_name="posts", blank=True, verbose_name=_("Tags"))

    image = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name=_("Post Image"))
    status = models.CharField(max_length=10, choices=PostStatus.choices, default=PostStatus.DRAFT, verbose_name=_("Status"))
    view_count = models.PositiveIntegerField(default=0, verbose_name=_("View Count"))
    is_featured = models.BooleanField(default=False, verbose_name=_("Is Featured"))
    published_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Published At"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class PostCategory(BaseModel):
    name = models.CharField(max_length=150, unique=True, verbose_name=_("Category Name"))
    slug = models.SlugField(verbose_name=_("slug"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("PostCategory")
        verbose_name_plural = _("PostCategories")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Tag Name"))
    slug = models.SlugField(verbose_name=_("slug"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name


class Comment(BaseModel):
    content = models.TextField(verbose_name=_("Comment Content"))

    post = models.ForeignKey("blog.BlogPost", on_delete=models.CASCADE, related_name="comments", verbose_name=_("Post"))
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="comments", verbose_name=_("Comment Author"))

    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies", verbose_name="Parent Comment")

    is_active = models.BooleanField(default=True, verbose_name=_("Active"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.user} on {self.post.title[:20]}"
