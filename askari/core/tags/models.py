from django.db import models
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class TagItem(models.Model):
    class Meta:
        unique_together = ('tag', 'content_type', 'object_id')

    tag = models.ForeignKey('Tag')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
