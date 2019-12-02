from django.test import TestCase, Client, RequestFactory
from products.models import Product, Category


class TestProductPages(TestCase):

    def setUp(self):
        self.client = Client()

    def test_allproduct_view_without_filter(self):
        page = self.client.get('/products/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_products.html')

    """
    Check that pagination function works correctly with the same
    template as the main allproduct view
    """
    def test_pagination_checker(self):
        page = self.client.get('/products/?page=3')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_products.html')

    def test_category_functionality(self):
        page = self.client.get('/products/?category=Furniture')
        self.assertEqual(page.status_code, 200)

    def test_detail_prod_view(self):
        """
        Create a category, create a product with that category
        try and access the page for this product.
        """
        cat = Category(category="testCat")
        cat.save()
        """testing this function started here, having to create a
        product and then making sure the NOT NULL fields were
        Filled and then the category object had its relational item
        in another area of the DB"""
        product = Product(title='TestProd',
                          price=24,
                          category=cat)
        product.save()
        id = product.id
        page = self.client.get('/products/more_info/{0}'.format(id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'prod_detail.html')
