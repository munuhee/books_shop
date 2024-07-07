import json
from orders.models import Order, OrderItem
from accounts.models import Customer
from store.models import Product


def cookieCart(request):
    """
    Retrieves and processes the cart data from cookies.

    Args:
    - request: HttpRequest object.

    Returns:
    - dict: Contains cartItems, order details, and items list.
    """
    cartItems = 0
    items = []
    order = {
        'get_cart_total': 0,
        'get_cart_items': 0,
        'shipping': False
    }

    try:
        cart = json.loads(request.COOKIES.get('cart', '{}'))
    except json.JSONDecodeError:
        cart = {}
        print('Error decoding cart JSON.')

    for i in cart:
        try:
            quantity = cart[i]['quantity']
            if quantity > 0:
                cartItems += quantity

                product = Product.objects.get(id=i)
                total = product.price * quantity

                order['get_cart_total'] += total
                order['get_cart_items'] += quantity

                item = {
                    'id': product.id,
                    'product': {
                        'id': product.id,
                        'name': product.name,
                        'price': product.price,
                        'imageURL': product.imageURL
                    },
                    'quantity': quantity,
                    'digital': product.digital,
                    'get_total': total,
                }
                items.append(item)

                if not product.digital:
                    order['shipping'] = True
        except Product.DoesNotExist:
            print(f'Product with id {i} does not exist.')
        except Exception as e:
            print(f'Error processing product id {i}: {str(e)}')

    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    """
    Retrieves cart data for authenticated or guest users.

    Args:
    - request: HttpRequest object.

    Returns:
    - dict: Contains cartItems, order details, and items list.
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
        )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    """
    Processes an order for a guest user.

    Args:
    - request: HttpRequest object.
    - data: dict with 'form' containing 'name' and 'email'.

    Returns:
    - tuple: Contains Customer and Order objects.
    """
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(email=email)
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        try:
            product = Product.objects.get(id=item['id'])
            quantity = item['quantity']
            if quantity > 0:
                OrderItem.objects.create(
                    product=product,
                    order=order,
                    quantity=quantity,
                )
        except Product.DoesNotExist:
            print(f'Product with id {item["id"]} does not exist.')

    return customer, order
