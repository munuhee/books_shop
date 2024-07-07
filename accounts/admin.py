from django.contrib import admin
from .models import Customer, Wishlist, Inbox, Message

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'phone_number_verified', 'otp')
    search_fields = ('user__username', 'phone_number')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'timestamp', 'is_read')
    search_fields = ('sender__username', 'receiver__username', 'subject')
    list_filter = ('is_read', 'timestamp')
