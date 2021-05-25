from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from ..views import post_list
from ..models import Post


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


class PostDetailTest(TestCase):
    def setUp(self):
        author = User.objects.create_user(username='test_user', password='django123')
        Post.objects.create(title='Post 1', slug='post-1', body='Post 1 body', author=author)

    def test_post_detail_status_code(self):
        post = Post.objects.get(id=1)
        response = self.client.get(post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
