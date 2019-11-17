from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product
# Create your views here.
def view_cart(request):
    """
    A view that renders the Users cart items
    Storing them for payment at checkout later
    """
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """
    Add a quantity of the product to the users cart
    """
    
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    messages.success(request, '%s x %s was added to the cart' % (quantity ,product.title))
    request.session['cart'] = cart
    return redirect(reverse('products'))


def remove_product(request, id):
    """
    View for button removing items from cart from the users stored items
    """
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    messages.success(request, '%s was removed from the cart' %(product.title))
    return redirect('view_cart')


def adjust_products(request, id):
    """
    Adjusts the users amount stored in cart of a specified
    product within that cart session
    """
    product = get_object_or_404(Product, pk=id)
    quantity = int(request.POST.get('quantity'))
    cart  = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else: 
        cart.pop(id)
    request.session['cart'] = cart
    messages.success(request, '%s was amended to %s' %(product.title, quantity))
    return redirect(reverse('view_cart'))