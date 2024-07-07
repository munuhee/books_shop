from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    CustomUserCreationForm,
    CustomerForm,
    UserForm,
    CustomAuthenticationForm
)


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
                return redirect('store')
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
            return redirect('customer_view')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/password_change.html', {'form': form})


@login_required
def customer_view(request):
    user = request.user
    customer = user.customer
    inbox_messages = user.inbox.messages.all()
    wishlist_items = user.wishlist.product.all()

    context = {
        'user': user,
        'customer': customer,
        'inbox_messages': inbox_messages,
        'wishlist_items': wishlist_items,
    }

    return render(request, 'accounts/customer_view.html', context)


@login_required
def customer_update(request):
    customer = request.user.customer
    user = request.user

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        user_form = UserForm(request.POST, instance=user)
        if customer_form.is_valid() and user_form.is_valid():
            customer_form.save()
            user_form.save()
            messages.success(request, 'Customer updated successfully!')
            return redirect('customer_view')
    else:
        customer_form = CustomerForm(instance=customer)
        user_form = UserForm(instance=user)

    context = {
        'customer_form': customer_form,
        'user_form': user_form,
    }

    return render(request, 'accounts/customer_update.html', context)
