# Generated by Django 4.2.3 on 2023-07-26 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0003_alter_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_products_qty',
        ),
    ]
