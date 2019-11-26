from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe


stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    """
    A complex view for ensuring that payment information is being 
    parsed to stripe and back to the browser correctly, resulting in
    a user being able to purchase items from the store and receiving 
    an order number (PK) of the order model
    """
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                if len(cart) > 0:
                    product = get_object_or_404(Product, pk=id)
                    total += quantity * product.price
                    order_line_item = OrderLineItem(
                        order = order,
                        product = product,
                        quantity = quantity
                    )
                    order_line_item.save()
                else:
                    messages.error(
                        request, 'Your cart is empty, head back to all products!')

                try:
                    customer = stripe.Charge.create(
                        amount = int(total*100),
                        currency = 'EUR',
                        description = request.user.email,
                        card = payment_form.cleaned_data['stripe_id'],
                    )
                except stripe.error.CardError:
                    messages.error(request, 'Your card was declined!')
                if customer.paid:
                    messages.error(request, 'You\'ve successfully paid')
                    request.session['cart'] = {}
                    return redirect(reverse('products'))
                else:
                    messages.error(request, 'We\'re unable to take your payment at this time.')
            else:
                print(payment_form.errors)
                messages.error(request, 'We\'re unable to take payment from this card.')
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    context = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE}
    return render(request, 'checkout.html', context)