# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from model_mommy import mommy

from .models import Database
from ..organizations.models import Organization
from ..core.user_profile.models import UserProfile


class DatabaseViewTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.organization = mommy.make(Organization, slug='foo_org')
        self.user = User.objects.create_user('test', 'test@test.com', '123456')
        self.user_profile = mommy.make(UserProfile, user=self.user)
        self.user.userprofile.organizations.add(self.organization)
        self.database = mommy.make(Database,
                                   user=self.user,
                                   organization=self.organization)

    def do_login(self):
        self.client.login(username='test', password='123456')

    def list_view_request(self):
        self.url = reverse('databases:list', kwargs={
            'organization': self.organization.slug})
        self.response = self.client.get(self.url)

    def new_view_request(self):
        self.url = reverse('databases:new', kwargs={
            'organization': self.organization.slug})
        self.response = self.client.get(self.url)

    def delete_view_request(self):
        self.url = reverse('databases:delete', kwargs={
            'pk': self.database.pk, 'organization': self.organization.slug})
        self.response = self.client.delete(self.url)

    def create_view_request(self):
        self.url = reverse('databases:new', kwargs={
            'organization': self.organization.slug})
        self.post_attributes = {'name': u'test',
                                'db_name': u'test',
                                'db_host': u'test',
                                'db_user': u'test',
                                'db_engine': u'postgres'}

        self.response = self.client.post(self.url, self.post_attributes)

    def test_new_view_without_login(self):
        self.new_view_request()

        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, "/login/?next={}".format(self.url))

    def test_new_view(self):
        self.do_login()
        self.new_view_request()

        self.assertEqual(self.response.status_code, 200)

    def test_create_view_without_login(self):
        self.create_view_request()

        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, "/login/?next={}".format(self.url))

    def test_create_view_should_add_loged_user_into_database(self):
        self.do_login()

        self.create_view_request()
        self.assertEqual(self.response.status_code, 302)

        database = Database.objects.filter(name=u'test').first()
        self.assertIsNotNone(database)
        self.assertEqual(self.user, database.user)

    def test_list_view_without_login(self):
        self.list_view_request()

        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, "/login/?next={}".format(self.url))

    def test_list_view(self):
        self.do_login()
        self.list_view_request()

        self.assertEqual(self.response.status_code, 200)
        self.assertIn(self.database.name, self.response.rendered_content)

    def test_delete_view_without_login(self):
        self.delete_view_request()

        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, "/login/?next={}".format(self.url))

    def test_delete_view(self):
        self.do_login()
        self.delete_view_request()

        list_url = reverse('databases:list', kwargs={
            'organization': self.organization.slug})

        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, list_url)

        self.list_view_request()
        self.assertNotIn(self.database.name, self.response.rendered_content)
