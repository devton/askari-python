# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.template.defaultfilters import slugify

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField("Nome", 
                            max_length=200, 
                            unique=True, 
                            db_index=True)

    slug = models.SlugField("Slug", db_index=True, max_length=150)

    __unicode__ = lambda self: self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        unique_together = ['slug', 'name']

@python_2_unicode_compatible
class Tagged(models.Model):
    tags = models.CharField("Tags", 
                            max_length=4000, 
                            blank=True,
                            null=True,
                            help_text="Lista de tags separadas por virgula")

    def save(self, *args, **kwargs):
        if self.tags:
            tags = filter(None, set(self.tags.split(',')))
            tags = map(str.strip, tags)

            for tag in tags:
                Tag.objects.get_or_create(name=tag)

            self.tags = ','.join(tags)

        super(Tagged, self).save(*args, **kwargs)

    def get_tags(self):
        if self.tags:
            tags = []

            for tag in self.tags.split(','):
                if tag in ["", " "]:
                    continue

                t, created = Tag.objects.get_or_create(name=tag)
                tags.append(t)

            return tags

    class Meta:
        abstract = True

