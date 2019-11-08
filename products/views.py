from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
        products = Product.objects.filter(category=category).order_by(products.pubd)


    if request.GET.getlist('category'):
        selected = Category.objects.filter(
            category__in=request.GET.getlist('category')).order_by(products.pubd)
        products = [product for product in products if product.category in selected].order_by(products.pubd)

    paginator = Paginator(products, 12)
    page = request.GET.get('page', 1)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


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
