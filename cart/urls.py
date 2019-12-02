from django.conf.urls import re_path
from .views import view_cart, add_to_cart, remove_product, adjust_products

urlpatterns = [
    re_path(r'^$', view_cart, name="view_cart"),
    re_path(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    re_path(r'^remove/(\d+)$', remove_product, name='remove_from_cart'),
    re_path(r'^change/(?P<id>\d+)', adjust_products, name="change_cart")
]
