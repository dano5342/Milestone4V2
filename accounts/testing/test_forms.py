from django.test import TestCase
from accounts.forms import UserRegistrationForm, UpdateForm, ProfileUpdate


class TestAccountForms(TestCase):
    def test_can_create_a_user(self):
        form = UserRegistrationForm({'username': 'user3',
                                     'email': 'test@email.com',
                                     'password1': 'testing321',
                                     'password2': 'testing321'})
        self.assertTrue(form.is_valid())

    def test_update_form(self):
        form = UpdateForm({'username': 'testuser',
                           'email': 'test@email.com'})
        self.assertTrue(form.is_valid())

    def test_profile_update_form(self):
        form = ProfileUpdate({'image':
                              'https://via.placeholder.com/350x65'})
        self.assertTrue(form.is_valid())
