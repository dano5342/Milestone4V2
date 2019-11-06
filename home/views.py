from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Category, Product
# Create your views here.
def index(request, category_name=None):
    """
    Displays all products (in future with pagination, and 
    category displays only displaying items within the category)
    """
    category = Category.objects.all()
    args = {'category': category}
    
    return render(request, 'index.html', args)