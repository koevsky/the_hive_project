# Generated by Django 4.2.3 on 2023-07-13 13:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apiary_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_type', models.CharField(choices=[('Honey', 'Honey'), ('Pollen', 'Pollen'), ('Propolis', 'Propolis')])),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('apiary', models.ManyToManyField(to='apiary_app.apiarymodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
