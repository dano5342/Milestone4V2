from django.test import TestCase, Client, RequestFactory
from accounts.views import register, profile
from django.contrib.auth.models import User
# Create your tests here.
class TestAccountsViewsOut(TestCase):
    def test_register_page(self):
        page = self.client.get('/accounts/register/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register.html')


    def test_login_page(self):
        page = self.client.get('/login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')


class TestAccountsViewsIn(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user789', email='test@user.com', password="456user"
        )
    
    def test_registration_page(self):
        request = self.factory.get('/')
        request.user = self.user
        response = register(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")