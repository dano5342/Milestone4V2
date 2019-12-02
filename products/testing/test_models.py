from django.test import TestCase
from products.models import Product, Category


class TestCategoryModel(TestCase):
    def test_create_category(self):
        cat = Category(
            category='TestC',
            image='https://via.placeholder.com/350x65',
            description='This is a test'
        )
        cat.save()
        self.assertEqual(cat.category, 'TestC')


class TestProductModel(TestCase):
    def test_create_product(self):
        pro = Product(title='TestProd')
        self.assertEqual(pro.title, 'TestProd')

    def test_prod_with_category(self):
        cat = Category(category="testCat")
        prod = Product(
            title='TestProduct',
            category=cat
        )
        self.assertEqual(str(prod.category), 'testCat')
