from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from model_mommy import mommy

from .models import Database


class DatabaseViewTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user('test', 'test@test.com', '123456')
        self.database = mommy.make(Database, user=self.user)

    def do_login(self):
        self.client.login(username='test', password='123456')

    def list_request(self):
        self.url = reverse('databases:list')
        self.response = self.client.get(self.url)

    def test_list_view_without_login(self):
        self.list_request()

        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, "/login/?next={}".format(self.url))

    def test_list_view(self):
        self.do_login()
        self.list_request()

        self.assertEqual(self.response.status_code, 200)
        self.assertIn(self.database.name, self.response.rendered_content)
