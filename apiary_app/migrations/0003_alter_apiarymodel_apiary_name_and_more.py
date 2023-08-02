# Generated by Django 4.2.3 on 2023-08-02 17:35

import apiary_app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiary_app', '0002_alter_apiarymodel_hives_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiarymodel',
            name='apiary_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), apiary_app.validators.validate_name_upper, apiary_app.validators.validate_name_symbols, apiary_app.validators.validate_is_whitespace]),
        ),
        migrations.AlterField(
            model_name='apiarymodel',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), apiary_app.validators.validate_name_upper, apiary_app.validators.validate_name_symbols, apiary_app.validators.validate_is_whitespace]),
        ),
    ]
