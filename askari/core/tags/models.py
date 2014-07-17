# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(u"Nome", 
                            max_length=200, 
                            unique=True, 
                            db_index=True)

    slug = models.SlugField(u"Slug", db_index=True, max_length=150)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        unique_together = ['slug', 'name']


class Tagged(models.Model):
    tags = models.CharField(u"Tags", 
                            max_length=4000, 
                            blank=True,
                            null=True,
                            help_text=u"Lista de tags separadas por virgula")

    def save(self, *args, **kwargs):
        if self.tags:
            tags = filter(None, set(self.tags.split(',')))
            tags = map(unicode.strip, tags)

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

