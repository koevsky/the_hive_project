# Generated by Django 4.2.3 on 2023-07-31 18:52

import accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_hiveuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiveuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), accounts.validators.validate_name_is_alpha, accounts.validators.validate_name_starts_with_upper]),
        ),
        migrations.AlterField(
            model_name='hiveuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), accounts.validators.validate_name_is_alpha, accounts.validators.validate_name_starts_with_upper]),
        ),
    ]
