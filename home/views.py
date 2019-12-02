from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Category, Product
from .forms import ContactForm


# Create your views here.
def index(request, category_name=None):
    """
    Displays the home page with categories and a short description
    """
    category = Category.objects.all()
    args = {'category': category}
    
    return render(request, 'index.html', args)


def about(request):
    """
    Sends the customer to the about us section
    """
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'about.html', context)


def jobs(request):
    """
    Sends to a 'blank' careers page for portfolio purposes only.
    """
    return render(request, 'jobs.html')


def contact(request):
    """
    Directs the customer to a contact us form
    """
    if request.method == 'GET':
        form = ContactForm()
    else: 
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            to_list = [form.from_email, settings.EMAIL_HOST_USER]

            send_mail(subject, from_email, message, to_list, fail_silently=False)
