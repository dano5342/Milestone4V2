from django.shortcuts import render, get_object_or_404
from products.models import Product, Category


# Create your views here.
def index(request, category_name=None):
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
            type__in=request.GET.getlist(category))
        products = [product for product in products if product.category in selected]
        print(products)
        print(selected)


    args = {'products': products, 'category': category}
    return render(request, 'index.html', args)