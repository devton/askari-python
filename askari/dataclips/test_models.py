from django.test import TestCase
from model_mommy import mommy
from .models import Clip


class ClipTest(TestCase):
    def setUp(self):
        self.clip = mommy.make(Clip, slug='')

    def test_slug_field_filled(self):
        self.clip.save()
        self.assertTrue(isinstance(self.clip, Clip))
        self.assertRegexpMatches(self.clip.slug, r'^\w{32}$')
