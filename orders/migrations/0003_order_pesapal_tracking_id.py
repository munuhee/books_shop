# Generated by Django 5.0.6 on 2024-07-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_paid_order_items_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pesapal_tracking_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]