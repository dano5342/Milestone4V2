from .views import index
from django.urls import path, re_path
from products.views import all_products

urlpatterns =[
    path('', index, name="home"),
]