# Generated by Django 4.2.3 on 2023-07-13 19:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0004_remove_productmodel_apiary_productmodel_apiary'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='grams',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
