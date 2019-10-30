from django.shortcuts import render
from products.models import Product


def search(request):
    pof = Product.objects.filter
    products = (pof(title__icontains=request.GET['q'])|
                pof(summary__icontains=request.GET['q'])|
                pof(description__icontains=request.GET['q']))
    context = {'products': products}
    return render(request, 'all_products.html', context)
