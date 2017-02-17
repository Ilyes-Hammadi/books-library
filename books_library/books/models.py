from __future__ import unicode_literals

from django.db import models

# Create your models here.
from taggit.managers import TaggableManager


class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    link_to_pdf = models.URLField()
    thumbnail = models.ImageField(upload_to='books-thumbnail/', default='books-thumbnail/default.jpg')

    tags = TaggableManager()

    def __str__(self):
        return self.title
