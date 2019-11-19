from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdate, UpdateForm, AddressUpdate

def register(request):
    """ 
    Registers a new user on the backend
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, please now login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    """
    Returns the Users profile page
    """
    if request.method == 'POST':
        update_form = UpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdate(request.POST, request.FILES,
                                     instance=request.user.profile)
        address_form = AddressUpdate(request.POST, instance=request.user.address)

        if update_form.is_valid() and profile_form.is_valid() and address_form.is_valid():
            update_form.save()
            profile_form.save()
            address_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        update_form = UpdateForm(instance=request.user)
        profile_form = ProfileUpdate(instance=request.user)
        address_form = AddressUpdate()

    form_contexts = {
        'update_form': update_form,
        'profile_form': profile_form,
        'address_form': address_form}
    return render(request, 'profile.html', form_contexts)
