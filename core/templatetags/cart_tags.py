from django import template
from django.db.models import Sum


register = template.Library()


@register.simple_tag(takes_context=True)
def cart_total_quantity(context):
    user = context['user']
    if user.is_authenticated:
        cart = user.cart
        total_quantity = cart.items.aggregate(
            total_quantity=Sum('quantity')
        )['total_quantity'] or 0
    else:
        total_quantity = 0
    return total_quantity
