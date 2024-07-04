import random
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Profile, Address, Message, Wishlist, Inbox


def generate_otp():
    """Generates a 6-digit OTP"""
    return str(random.randint(100000, 999999))


# Create or update user profile and send OTP email
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        Wishlist.objects.create(user=instance)
        Inbox.objects.create(user=instance)

        # Generate OTP
        otp = generate_otp()
        profile.otp = otp
        profile.save()

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
        instance.profile.save()


# Ensure there's only one default address per user
@receiver(post_save, sender=Address)
def set_default_address(sender, instance, **kwargs):
    if instance.default:
        Address.objects.filter(
            user=instance.user
            ).exclude(id=instance.id).update(
            default=False
        )


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


# Delete related addresses when a user is deleted
@receiver(post_delete, sender=User)
def delete_related_addresses(sender, instance, **kwargs):
    addresses = Address.objects.filter(user=instance)
    for address in addresses:
        address.delete()


# Ensure there's only one default address when an address is deleted
@receiver(post_delete, sender=Address)
def ensure_one_default_address(sender, instance, **kwargs):
    user_addresses = Address.objects.filter(user=instance.user)
    if (
        user_addresses.filter(default=True).count() == 0 and
        user_addresses.exists()
    ):
        first_address = user_addresses.first()
        first_address.default = True
        first_address.save()
