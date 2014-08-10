from __future__ import unicode_literals
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name
