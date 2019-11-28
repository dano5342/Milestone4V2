from django.test import TestCase
from checkout.forms import OrderForm


"""
I'm not entirely sure how to test the stripe API keys within
a django test, This however was manually tested with the given
stripe test card numbers. Document this in the README.MD
"""

class TestOrderForm(TestCase):
    

    def test_order_form_is_valid(self):
        form = OrderForm({
            'full_name': 'user432',
            'phone_number': '+4477332233445',
            'country': 'Germany',
            'postcode': '10023',
            'city_or_town': 'Berlin',
            'address1': 'address1',
            'address2': 'address2',
            'county': 'Brandenberg'
        })

        self.assertTrue(form.is_valid())
