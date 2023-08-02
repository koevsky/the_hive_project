# Generated by Django 4.2.3 on 2023-08-02 20:36

import django.core.validators
from django.db import migrations, models
import product_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0010_alter_productmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_name',
            field=models.CharField(max_length=60, unique=True, validators=[product_app.validators.product_name_validator, django.core.validators.MinLengthValidator(3)]),
        ),
    ]
