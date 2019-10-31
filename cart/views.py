from django.shortcuts import render, redirect, reverse

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

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def remove_product(request, id):
    """
    View for button removing items from cart from the users stored items
    """
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')


def adjust_products(request, id):
    """
    Adjusts the users amount stored in cart of a specified
    product within that cart session
    """
    quantity = int(request.POST.get('quantity'))
    cart  = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else: 
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))