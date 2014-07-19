from django.test import TestCase
from django.contrib.auth import get_user_model

from ..databases.models import Database
from .models import Clip


class ClipTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username=u'test', password='test')
        self.database = Database.objects.create(user=self.user)
        self.clip = Clip.objects.create(name='foo', database=self.database)

    def test_slug_field_filled(self):
        self.assertRegexpMatches(self.clip.slug, r'^\w{32}$')
