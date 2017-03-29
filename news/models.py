# future
from __future__ import unicode_literals

# Django
from django.db import models


class NewsDetails(models.Model):
    category = models.CharField(max_length=30)
    video_id = models.CharField(max_length=30)
    StoryImage = models.CharField(max_length=300)
    description = models.CharField(max_length=3000)
    pubDate = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    fullimage = models.CharField(max_length=400)
    source = models.CharField(max_length=40)
    link = models.CharField(max_length=400)
    updatedAt = models.CharField(max_length=40)
