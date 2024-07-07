from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'customer', 'date_ordered', 'complete', 'transaction_id'
    )
    list_filter = ('complete', 'date_ordered')
    search_fields = ('customer__name', 'transaction_id')
    readonly_fields = ('id', 'date_ordered', 'transaction_id')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'date_added')
    list_filter = ('product', 'date_added')
    search_fields = ('order__id', 'product__name')


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 'order', 'address',
        'city', 'state', 'zipcode', 'date_added'
        )
    list_filter = ('city', 'state')
    search_fields = ('customer__name', 'address', 'zipcode')
