from django.shortcuts import render
from .models import Product, Category
# Create your views here.
def all_products(request, category_id=None):
    """
    Displays all products (in future with pagination, and 
    category displays only displaying items within the category)
    """

    if not category_id:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(Category, category_id)
    prod_args = {"products": products}
    return render(request, "products.html", prod_args)
