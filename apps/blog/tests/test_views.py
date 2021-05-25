from django.test import TestCase
from django.urls import reverse, resolve

from ..views import post_list


class PostListTest(TestCase):
    def test_post_list_status_code(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_name(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_template(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/post/list.html')

    def test_post_list_use_correct_view(self):
        view = resolve('/blog/')
        self.assertEqual(view.func.__name__, post_list.__name__)
