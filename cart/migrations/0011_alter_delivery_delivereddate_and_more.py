# Generated by Django 4.0.1 on 2022-02-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_remove_order_delivered_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='deliveredDate',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='deliveryDate',
            field=models.DateTimeField(blank=True),
        ),
    ]
