# Generated by Django 4.2.3 on 2023-07-20 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0008_alter_productmodel_product_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hive_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
