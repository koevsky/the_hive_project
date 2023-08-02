# Generated by Django 4.2.3 on 2023-08-02 20:36

import apiary_app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiary_app', '0003_alter_apiarymodel_apiary_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiarymodel',
            name='apiary_name',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), apiary_app.validators.validate_name_upper, apiary_app.validators.validate_name_symbols, apiary_app.validators.validate_is_whitespace]),
        ),
    ]