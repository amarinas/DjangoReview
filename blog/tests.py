from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model

# Create your tests here.
class PostModelTest(TestCase):

    def test_string_representation(self):
        post = Post(title="My Post title")
        self.assertEqual(str(post), post.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Post._meta.verbose_name_plural), "posts")

    class Meta:
        verbose_name_plural = "posts"

class ProjectTest(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class HomePageTests(TestCase):

    """Test whether our blog entries show up on the homepage"""

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_one_entry(self):
        Post.objects.create(title='title', text='text', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, 'title')
        self.assertContains(response, 'text')

    def test_two_entries(self):
        Post.objects.create(title='title', text='text', author=self.user)
        Post.objects.create(title='title', text='text', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, 'title')
        self.assertContains(response, 'text')
        self.assertContains(response, 'title')
