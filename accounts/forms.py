from django import forms
from .models import Profile, UserAddress
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username', 'email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class AddressUpdate(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['address1', 'address2', 'city_or_town', 'county',
                   'country', 'zip_or_postcode']