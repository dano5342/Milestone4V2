from django.shortcuts import render
from products.models import Product, Category


def search(request):
    category = Category.objects.all()
    pof = Product.objects.filter
    products = (pof(title__icontains=request.GET['q'])|
                pof(summary__icontains=request.GET['q'])|
                pof(description__icontains=request.GET['q']))
    context = {'products': products, 'category': category}
    return render(request, 'all_products.html', context)
