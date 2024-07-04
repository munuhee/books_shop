from django.contrib import admin
from .models import Profile, Address, Wishlist, Inbox, Message


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone_number',
        'phone_number_verified',
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'street_address',
        'apartment_address',
        'city',
        'state',
        'country',
        'zip',
        'address_type',
        'default',
    )


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'sender',
        'receiver',
        'subject',
        'timestamp',
        'is_read',
    )
