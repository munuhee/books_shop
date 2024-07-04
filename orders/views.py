import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseServerError
from decimal import Decimal
from .models import Order, OrderItem
from cart.models import Cart


def calculate_total_amount(cart):
    total_amount = 0
    for item in cart.items.all():
        total_amount += item.quantity * item.ebook.price
    return total_amount


@login_required
@transaction.atomic
def create_order(request):
    try:
        cart = get_object_or_404(Cart, user=request.user)

        # Ensure cart items exist before proceeding
        if not cart.items.exists():
            raise Exception("Cart is empty. Cannot create order.")

        total_amount = calculate_total_amount(cart)

        order = Order.objects.create(
            user=request.user,
            total_amount=total_amount
        )

        # Adding cart items to the order
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                ebook=cart_item.ebook,
                quantity=cart_item.quantity
            )

        # Clear cart items after successful order creation
        cart.items.all().delete()

        # Redirect to a view where the user can view the order details
        return redirect('order_details', order_id=order.id)

    except Exception as e:
        return HttpResponseServerError(f"Error creating order: {str(e)}")


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'orders': orders
    }
    return render(request, 'orders/order_list.html', context)


@login_required
def order_details(request, order_id):
    try:
        order = Order.objects.get(id=order_id, user=request.user)
        order_items = order.items.all()
        user = request.user
        addresses = user.addresses.all()

        # Ensure all monetary values are Decimal
        subtotal = Decimal(order.total_amount)
        shipping = Decimal('8.00')
        total = subtotal + shipping

        context = {
            'order': order,
            'addresses': addresses,
            'order_items': order_items,
            'subtotal': subtotal,
            'shipping': shipping,
            'total': total,
        }

        return render(request, 'orders/checkout.html', context)

    except Order.DoesNotExist:
        return HttpResponseServerError("Order not found.")


def get_pesapal_token():
    """Obtain an access token from Pesapal."""
    try:
        url = (
            settings.PESAPAL_AUTH_URL_DEMO if settings.
            PESAPAL_DEMO else settings.PESAPAL_AUTH_URL_PROD
        )
        payload = {
            "consumer_key": settings.PESAPAL_CONSUMER_KEY,
            "consumer_secret": settings.PESAPAL_CONSUMER_SECRET
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        return response_data['token']
    except requests.RequestException:
        return None


def register_ipn_url():
    """Register the IPN URL with Pesapal."""
    try:
        url = (
            settings.PESAPAL_IPN_URL_DEMO if settings.
            PESAPAL_DEMO else settings.PESAPAL_IPN_URL_PROD
        )
        token = get_pesapal_token()
        if not token:
            raise Exception("Failed to obtain Pesapal token")
        payload = {
            "url": settings.PESAPAL_IPN_URL,
            "ipn_notification_type": "GET"
        }
        headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        return response_data['ipn_id']
    except requests.RequestException:
        return None


@login_required
def initiate_pesapal_checkout(request, order_id):
    """Initiate the Pesapal checkout process for an order."""
    try:
        order = get_object_or_404(Order, id=order_id, user=request.user)
        token = get_pesapal_token()
        if not token:
            raise Exception("Failed to obtain Pesapal token")
        ipn_id = register_ipn_url()
        if not ipn_id:
            raise Exception("Failed to register IPN URL")

        url = (
            settings.PESAPAL_ORDER_URL_DEMO if settings.
            PESAPAL_DEMO else settings.PESAPAL_ORDER_URL_PROD
        )
        payload = {
            "id": str(order.id),
            "currency": "KES",
            "amount": str(order.total_amount),
            "description": f"Payment for Order #{order.id}",
            "callback_url": settings.PESAPAL_CALLBACK_URL,
            "notification_id": ipn_id,
            "billing_address": {
                "email_address": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name
            }
        }
        headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        if response.status_code == 200:
            return redirect(response_data['redirect_url'])
        else:
            return render(
                request,
                'order/payment_error.html',
                {'error': response_data.get(
                    'message', 'An error occurred'
                )}
            )
    except Exception as e:
        return render(request, 'order/payment_error.html', {'error': str(e)})
