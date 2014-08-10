# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from model_mommy import mommy
from .models import Clip
from ..organizations.models import Organization
from ..core.user_profile.models import UserProfile


class ClipViewTest(TestCase):
    def setUp(self):
        self.organization = mommy.make(Organization, slug='foo_org')
        self.user = User.objects.create_user('test', 'test@test.com', '123456')
        self.user_profile = mommy.make(UserProfile, user=self.user)
        self.user.userprofile.organizations.add(self.organization)
        self.clip = mommy.make(Clip, 
                               database__user=self.user, 
                               slug='abcd', 
                               organization=self.organization)

        stub = lambda self: {'cols': [u'cols'], 'rows': [[u'rows']]}
        Clip.query_result = stub

    def do_login(self):
        self.client.login(username='test', password='123456')

    def test_clip_in_list_view(self):
        self.do_login()

        url = reverse('dataclips:list', kwargs={
            'organization': self.organization.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.clip.name, response.rendered_content)

    def test_clip_in_public_view(self):
        self.do_login()

        url = reverse('dataclips:public', kwargs={
            'slug': self.clip.slug, 'organization': self.organization.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.clip.name, response.rendered_content)
        self.assertIn(u'rows', response.rendered_content)
        self.assertIn(u'cols', response.rendered_content)
