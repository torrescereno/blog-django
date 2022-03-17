from django.test import TestCase
from blog.models import Author
from blog.views import get_author
from django.contrib.auth.models import User


class AuthorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password="admin")
        self.autor = Author.objects.create(user=self.user)

    def test_get_author(self):

        author = get_author(self.user)
        self.assertEqual(author.user.username, "admin")
