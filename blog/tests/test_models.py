from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Post

User = get_user_model()


class TestPostModel(TestCase):
    """Test for Blog Model"""

    def setUp(self):
        user_data = {
            "username": "test_user",
            "email": "test@example.com",
            "password": "testpass",
            # "confirm_password": "test_pass"
        }
        self.user = User.objects.create(**user_data)
        self.first_data = {
            "author": self.user,
            "title": "Title One",
            "content": "First First First First First First First First First First First First"
        }
        self.second_data = {
            "author": self.user,
            "title": "Title Two",
            "content": "Second Second Second Second Second Second Second Second Second Second"
        }

    @staticmethod
    def create_post(data):
        """
        staticmethod to create post
        :param data: dictionary consists of Post model field
        :return: Post model object
        """
        return Post.objects.create(**data)

    def test_blog_creating(self):
        self.create_post(self.first_data)
        self.create_post(self.second_data)

        self.assertEqual(Post.objects.count(), 2)

    def test_blog_str(self):
        """
        Tests that model __str___ working properly
        """
        first_post = self.create_post(self.first_data)
        second_post = self.create_post(self.second_data)
        self.assertEqual(str(first_post), "Title One")
        self.assertEqual(str(second_post), "Title Two")

