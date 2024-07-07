import random
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Customer, Message, Wishlist, Inbox


def generate_otp():
    """Generates a 6-digit OTP"""
    return str(random.randint(100000, 999999))


# Create or update user customer and send OTP email
@receiver(post_save, sender=User)
def create_or_update_customer(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.create(user=instance)
        Wishlist.objects.create(user=instance)
        Inbox.objects.create(user=instance)

        # Generate OTP
        otp = generate_otp()
        customer.otp = otp
        customer.save()

        # Send OTP email
        subject = 'Verify Your Email Address'
        message = f'Your OTP for verifying your email address is: {otp}'
        recipient_list = [instance.email]
        send_mail(
            subject,
            message,
            'from@example.com',
            recipient_list,
            fail_silently=False
        )
    else:
        instance.customer.save()


# Send email notification when a message is sent
@receiver(post_save, sender=Message)
def send_message_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'New message from {instance.sender.username}'
        message = (
            f'You have received a new message from'
            f'{instance.sender.username}:\n\n'
            f'{instance.message}'
        )
        recipient_list = [instance.receiver.email]
        send_mail(
            subject,
            message,
            'from@example.com',
            recipient_list,
            fail_silently=False
        )
