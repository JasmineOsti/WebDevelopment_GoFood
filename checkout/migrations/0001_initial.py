# Generated by Django 3.2.4 on 2022-01-21 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0004_auto_20220119_1928'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('postalcode', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.shippingcontactinfo')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order')),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
