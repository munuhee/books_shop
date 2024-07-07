from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg '
                     'focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg '
                     'focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg '
                     'focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg '
                     'focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg '
                     'focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg '
                     'focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 '
                     'border border-gray-200 placeholder-gray-500 text-sm '
                     'focus:outline-none focus:border-gray-400 focus:bg-white',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 '
                     'border border-gray-200 placeholder-gray-500 text-sm '
                     'focus:outline-none focus:border-gray-400 focus:bg-white',
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


class CustomerForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=False, validators=[
        RegexValidator(
            r'^\+?1?\d{9,15}$',
            message="Phone number must be valid."
        )
    ])

    class Meta:
        model = Customer
        fields = ['phone_number']
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded border border-gray-300',
                'placeholder': 'Phone number'
            }),
        }
