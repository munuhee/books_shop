from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .models import Cart, CartItem
from ebooks.models import EBook

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})

@require_POST
def add_to_cart(request, ebook_id):
    ebook = get_object_or_404(EBook, id=ebook_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, ebook=ebook)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return JsonResponse({'success': True})

@require_GET
def remove_from_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
        return JsonResponse({'success': True})
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'CartItem not found'})

@require_POST
def update_cart(request):
    try:
        cart_item_id = request.POST.get('item_id')
        new_quantity = int(request.POST.get('new_quantity'))
        cart_item = CartItem.objects.get(id=cart_item_id)
        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()
        else:
            cart_item.delete()
        return JsonResponse({'success': True})
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'CartItem not found'})
