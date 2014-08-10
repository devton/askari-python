from django.test import TestCase
from model_mommy import mommy
from .models import Organization


class OrganizationModelTest(TestCase):
    def setUp(self):
        self.org = mommy.make(Organization)

    def test_unicode(self):
        self.assertEqual(self.org.__unicode__(), self.org.name)
