from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile, create_profile



class TestAccountModels(TestCase):
    def test_profile_model(self):
        username = User.objects.create_user(
            username='user789', email='test@user.com', password='456user'
        )
        username.save()
        self.assertEqual(str(username), 'user789')

    def test_create_profile(self):
        self.assertTrue('created')