from .models import Tag, TagItem
from django.contrib.contenttypes.models import ContentType


def apply_tags(obj, tags):
    """ 
      Delete old tags and apply the new tags on object
    """

    kclass = ContentType.objects.get_for_model(obj)
    TagItem.objects.filter(content_type=kclass, object_id=obj.pk).delete()

    for tag_name in tags.split(','):
        tag, new_tag = Tag.objects.get_or_create(name=tag_name)
        TagItem.objects.get_or_create(
            tag=tag, 
            content_type=kclass, 
            object_id=obj.id,
            )


def tags_for(obj):
    """ 
      Get tags associated to object
    """

    kclass = ContentType.objects.get_for_model(obj)
    tags = TagItem.objects.filter(content_type=kclass, object_id=obj.pk)

    return ', '.join([item.tag.name for item in tags])
