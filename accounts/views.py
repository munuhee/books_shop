from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    CustomUserCreationForm,
    ProfileForm,
    UserForm,
    AddressForm,
    CustomAuthenticationForm
)
from .models import Address


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ebook_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your password was successfully updated!'
            )
            return redirect('profile_view')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/password_change.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    profile = user.profile
    addresses = user.addresses.all()
    inbox_messages = user.inbox.messages.all()
    wishlist_items = user.wishlist.ebooks.all()

    context = {
        'user': user,
        'profile': profile,
        'addresses': addresses,
        'inbox_messages': inbox_messages,
        'wishlist_items': wishlist_items,
    }

    return render(request, 'accounts/profile_view.html', context)


@login_required
def profile_update(request):
    profile = request.user.profile
    user = request.user

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        user_form = UserForm(request.POST, instance=user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_view')
    else:
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=user)

    context = {
        'profile_form': profile_form,
        'user_form': user_form,
    }

    return render(request, 'accounts/profile_update.html', context)


@login_required
def address_update(request, address_id):
    address = get_object_or_404(Address, id=address_id)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Address updated successfully!')
            return redirect('profile_view')
    else:
        form = AddressForm(instance=address)

    return render(request, 'accounts/address_update.html', {'form': form})
