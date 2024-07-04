from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
        blank=True
    )
    phone_number_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


ADDRESS_TYPE_CHOICES = (
    ('S', 'Shipping'),
    ('B', 'Billing')
)


class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses'
    )
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    address_type = models.CharField(
        max_length=1,
        choices=ADDRESS_TYPE_CHOICES
    )
    default = models.BooleanField(default=False)

    def __str__(self):
        return (
            f'{self.user.username}\'s'
            f'{self.get_address_type_display()} Address'
        )


class Wishlist(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='wishlist',
        verbose_name="User's Wishlist"
    )
    ebooks = models.ManyToManyField(
        'ebooks.EBook',
        related_name='wishlists',
        blank=True
    )

    def __str__(self):
        return f'{self.user.username}\'s Wishlist'


class Inbox(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='inbox',
        verbose_name="User's Inbox"
    )
    messages = models.ManyToManyField(
        'Message',
        related_name='inboxes',
        blank=True
    )

    def __str__(self):
        return f'{self.user.username}\'s Inbox'


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='sent_messages',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        related_name='received_messages',
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return (
            f'{self.sender.username} to'
            f'{self.receiver.username}: {self.subject}'
        )
