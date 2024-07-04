from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'created_at', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['id', 'user__username']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'ebook', 'quantity']
    list_filter = ['order__status']
    search_fields = ['order__id', 'ebook__title']
