from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from model_mommy import mommy
from django.test import TestCase
from django.db import IntegrityError

from .models import Tag
from askari.dataclips.models import Clip

@python_2_unicode_compatible
class TagTest(TestCase):
    def setUp(self):
        self.clip = mommy.make(Clip, tags="foo, bar")

    def test_clip_as_saving_tags_into_tags(self):
        total_tags = Tag.objects.count()
        self.assertEqual(total_tags, 2)

    def test_unicode(self):
        tag = Tag.objects.first()
        self.assertEqual(tag.__unicode__(), tag.name)

    def test_tag_slug(self):
        tag = mommy.make(Tag, name="Lorem ipsum", slug=None)
        self.assertEqual(tag.slug, "lorem-ipsum")

    def test_clip_get_tags(self):
        tag_foo = Tag.objects.filter(name="foo").first()
        tag_bar = Tag.objects.filter(name="bar").first()

        self.assertIn(tag_foo, self.clip.get_tags())
        self.assertIn(tag_bar, self.clip.get_tags())

    def test_unique(self):
        with self.assertRaises(IntegrityError):
            mommy.make(Tag, name='foo')
