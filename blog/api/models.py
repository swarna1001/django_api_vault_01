from django.db import models
from django.template.defaultfilters import slugify


def create_slug(title):

    title = str(title)
    new_slug = title.replace(".", "_")
    return new_slug


class BlogPost(models.Model):

    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    def get_absolute_url(self):
        return "/articles/{}".format(self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
