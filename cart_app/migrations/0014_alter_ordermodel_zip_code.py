# Generated by Django 4.2.3 on 2023-07-18 13:00

import cart_app.vlidators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0013_alter_ordermodel_cvv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='zip_code',
            field=models.CharField(validators=[cart_app.vlidators.zip_code_length]),
        ),
    ]
