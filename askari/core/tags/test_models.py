from model_mommy import mommy
from django.test import TestCase

from .models import Tag
from askari.dataclips.models import Clip


class TagTest(TestCase):
    def setUp(self):
        self.clip = mommy.make(Clip, tags=u"foo, bar")

    def test_clip_as_saving_tags_into_tags(self):
        total_tags = Tag.objects.count()
        self.assertEqual(total_tags, 2)

    def test_unicode(self):
        tag = Tag.objects.first()
        self.assertEqual(tag.__unicode__(), tag.name)

    def test_tag_slug(self):
        tag = mommy.make(Tag, name=u"Lorem ipsum", slug=None)
        self.assertEqual(tag.slug, u"lorem-ipsum")

    def test_clip_get_tags(self):
        tag_foo = Tag.objects.filter(name=u"foo").first()
        tag_bar = Tag.objects.filter(name=u"bar").first()

        self.assertIn(tag_foo, self.clip.get_tags())
        self.assertIn(tag_bar, self.clip.get_tags())
