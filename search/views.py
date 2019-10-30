from django.shortcuts import render
from products.models import Product


def search(request):
    products = Product.objects.filter(title__icontains=request.GET['q'])
    context = {'products': products}
    return render(request, 'all_products.html', context)
