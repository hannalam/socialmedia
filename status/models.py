from django.db import models

# I wrote this code

from django.conf import settings
from pyexpat import model
from django.utils.text import slugify

# model for the status and posts setup


class Status(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%M/%D')
    title = models.CharField(max_length=100)
    caption = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='likecount', blank=True)

    # show the status title in the admin page
    def __str__(self):
        return self.title

    # save the slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# end of code I wrote
