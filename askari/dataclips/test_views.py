# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from model_mommy import mommy
from .models import Clip


class ClipViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', '123456')
        self.clip = mommy.make(Clip, database__user=self.user, slug='abcd')
        stub = lambda self: {'cols': [u'cols'], 'rows': [[u'rows']]}
        Clip.query_result = stub

    def do_login(self):
        self.client.login(username='test', password='123456')

    def test_clip_in_list_view(self):
        self.do_login()

        url = reverse('dataclips:list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.clip.name, response.rendered_content)

    def test_clip_in_public_view(self):
        self.do_login()

        url = reverse('dataclips:public', kwargs={'slug': self.clip.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.clip.name, response.rendered_content)
        self.assertIn(u'rows', response.rendered_content)
        self.assertIn(u'cols', response.rendered_content)
