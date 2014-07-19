from django.test import TestCase
from django.contrib.auth import get_user_model
from model_mommy import mommy
from .models import Clip


class ClipModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.clip = mommy.make(Clip, slug='')
        self.user = mommy.make(User)

    def test_slug_field_filled(self):
        self.clip.save()
        self.assertTrue(isinstance(self.clip, Clip))
        self.assertRegexpMatches(self.clip.slug, r'^\w{32}$')

    def test_by_user_manager(self):
        mommy.make(Clip, database__user=self.user, _quantity=4)
        mommy.make(Clip, _quantity=4)

        self.assertEqual(Clip.objects.by_user(self.user).count(), 4)
