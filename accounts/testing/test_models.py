from django.test import TestCase
from accounts.models import Profile, create_profile
from .test_views import logged_in_user


class TestAccountModels(TestCase):
    def test_profile_model(self):
        username = logged_in_user
        username.save()
        self.assertEqual(username, 'user789')

    def test_create_profile(self):
        self.assertTrue('created')