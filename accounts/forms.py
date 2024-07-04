from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, Address


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'Last name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'Email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': '******************'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': '******************'
            })
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white',
            'placeholder': 'Password'
        })
    )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'Last name'
            }),
        }

class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=False, validators=[
        RegexValidator(
            r'^\+?1?\d{9,15}$',
            message="Phone number must be valid."
        )
    ])

    class Meta:
        model = Profile
        fields = ['phone_number']
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'Phone number'
            }),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'street_address',
            'apartment_address',
            'city',
            'state',
            'country',
            'zip',
            'address_type',
            'default'
        ]
        widgets = {
            'street_address': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'Street address'
            }),
            'apartment_address': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'Apartment address'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'City'
            }),
            'state': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'State'
            }),
            'country': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'Country'
            }),
            'zip': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'ZIP'
            }),
            'address_type': forms.Select(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
            }),
            'default': forms.CheckboxInput(attrs={
                'class': 'w-auto h-auto p-2 rounded border border-gray-300',
            }),
        }
