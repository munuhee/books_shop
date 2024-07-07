from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product
from core.utils import cartData


def store(request):
    """
    Render the store page with products and handle payment submission.
    """
    # Retrieve cart data
    data = cartData(request)
    cartItems = data['cartItems']

    # Retrieve all products
    products = Product.objects.all()

    # Apply search filter if query parameter exists
    query = request.GET.get('query')
    if query:
        products = products.filter(name__icontains=query)

    # Paginate products
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # Prepare context for rendering
    context = {
        'products': products,
        'cartItems': cartItems,
    }

    return render(request, 'store/store.html', context)


def product_detail(request, product_id):
    """
    Render the product detail page for a specific product.
    """
    # Retrieve product details or return 404 if not found
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)
