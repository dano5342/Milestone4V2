from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User


class TestCheckoutViewOut(TestCase):

    def setUp(self):
        self.client = Client()

    """
    Check that users get redirected to the login
    page for going through the checkout
    """
    def test_checkout_redir(self):
        page = self.client.get('/checkout/')
        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, '/login/?next=/checkout/')


class TestCheckoutViewIn(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user789', email='test@user.com', password='456user'
        )

    def test_checkout_view(self):
        client = Client()
        client.login(username='user789', password='456user')
        page = client.get('/checkout/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'checkout.html')
