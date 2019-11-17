from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product, Category
from django.views.generic import DetailView
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
        products = Product.objects.filter(category=category).order_by('-pubd')


    if request.GET.getlist('category'):
        selected = Category.objects.filter(
            category__in=request.GET.getlist('category'))
        products = [product for product in products if product.category in selected]

    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


    args = {'products': products, 'category': category}
    return render(request, 'all_products.html', args)


class MoreInfo(DetailView):
    """
    This view is for seeing more detail into the product
    The detailed description is removed from the homepage
    so it is added here. ALso for viewing extra products
    similar to that being viewed.
    """

    model = Product
    template_name = 'prod_detail.html'
    context_object_name = 'product'
    extra_context = {}


    def get_object(self, queryset=Product):
        _id = self.kwargs.get('pk')
        instance = get_object_or_404(Product, id=_id)

        self.extra_context['product'] = instance
        self.extra_context['more_prods'] = Product.objects.all().filter(category=instance.category).exclude(id=_id).order_by('-pubd')[:6]
        self.extra_context['category'] = Category.objects.all()
        return instance



    def post(self, request, *args, **kwargs):
        _id = self.kwargs.get('pk')
        instance = get_object_or_404(Product, id=_id)
        product = self.get_object()
        category = self.category
        return redirect(reverse('prod_detail.html', kwargs={'pk': product.pk}))