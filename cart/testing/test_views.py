from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from cart.contexts import cart_contents


class TestCartViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user789', email='test@user.com', password="456user"
        )

    def test_cart_view_empty(self):
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')

    """
    Now we've established that the cart page is accessible with a
    user in the DB, lets check if the cart contents is accessible
    we can run CRUD ops on them
    """


class TestCartFunctions(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.cart_contents = 0

    def test_empty_cart(self):
        cart_contents = 0
        self.assertEqual(cart_contents, 0)
