from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product, Category
# Create your views here.
def all_products(request, category_name=None):
    """
    Displays all products (in future with pagination, and 
    category displays only displaying items within the category)
    """
    products = Product.objects.all()
    category = Category.objects.all()
    selected = None


    if category_name:
        category = get_object_or_404(Category, category_name)
        products = Product.objects.filter(category=category)


    if request.GET.getlist('category'):
        selected = Category.objects.filter(
            category__in=request.GET.getlist(category))
        print(category)
        products = [product for product in products if product.category in selected]


    args = {'products': products, 'category': category}
    return render(request, 'all_products.html', args)


def more_info(request, product_id):
    """
    This view is for seeing more detail into the product
    The detailed description is removed from the homepage
    so it is added here.
    """
    product = get_object_or_404(Product, pk=product_id)
    detailed_args = {'product': product, 'product_id': product_id}
    return render(request, "prod_detail.html", detailed_args)
