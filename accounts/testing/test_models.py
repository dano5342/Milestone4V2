from django.test import TestCase
from accounts.models import Profile, create_profile
# Create your tests here.

class TestAccountModels(TestCase):
    def test_profile_model(self):
        username = Profile.user(username="testuser")
        username.save()
        self.assertEqual(username, 'testuser')

    def test_create_profile(self):
        self.assertTrue('created')