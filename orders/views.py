from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from .models import Order, OrderItem, ShippingAddress
from store.models import Product
from core.utils import cartData, guestOrder


def cart(request):
    """
    Renders the shopping cart page with current cart data.
    """
    data = cartData(request)
    context = {
        'items': data['items'],
        'order': data['order'],
        'cartItems': data['cartItems']
    }
    return render(request, 'orders/cart.html', context)


def checkout(request):
    """
    Renders the checkout page with current cart data.
    """
    data = cartData(request)
    context = {
        'items': data['items'],
        'order': data['order'],
        'cartItems': data['cartItems']
    }
    return render(request, 'orders/checkout.html', context)


def updateItem(request):
    """
    Updates the quantity of an item in the cart.
    Expects JSON data containing productId and action (add/remove).
    """
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer,
        complete=False
    )

    orderItem, created = OrderItem.objects.get_or_create(
        order=order,
        product=product
    )

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    if orderItem.quantity <= 0:
        orderItem.delete()
    else:
        orderItem.save()

    return JsonResponse('Item updated', safe=False)


def processOrder(request):
    """
    Processes a new order, handling both authenticated and guest users.
    Expects JSON data with order details including shipping information.
    """
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
        )
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total():
        order.complete = True
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment processed', safe=False)
