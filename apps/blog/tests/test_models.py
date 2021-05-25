from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Post


class PostModelTest(TestCase):
    def setUp(self):
        author = User.objects.create_user(username='test_user', password='django123')
        Post.objects.create(title='Post 1', slug='post-1', body='Post 1 body', author=author)

    def test_post_content(self):
        post = Post.objects.get(id=1)
        title = post.title
        slug = post.slug
        body = post.body
        author = post.author.username

        self.assertEqual(title, 'Post 1')
        self.assertEqual(slug, 'post-1')
        self.assertEqual(body, 'Post 1 body')
        self.assertEqual(author, 'test_user')

