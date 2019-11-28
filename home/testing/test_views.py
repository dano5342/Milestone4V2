from django.test import TestCase

# Create your tests here.

class TestHomeView(TestCase):

    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')