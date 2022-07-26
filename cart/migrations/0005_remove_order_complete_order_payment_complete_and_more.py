# Generated by Django 4.0.1 on 2022-01-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20220119_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('Khalti', 'Khalti')], default='Cash on Delivery', max_length=20),
        ),
    ]
