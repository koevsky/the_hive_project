# Generated by Django 4.2.3 on 2023-07-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiveuser',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
