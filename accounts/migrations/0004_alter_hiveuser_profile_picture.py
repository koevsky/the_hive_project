# Generated by Django 4.2.3 on 2023-07-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_hiveuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiveuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
