# Generated by Django 3.2.4 on 2022-01-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='product_imgs'),
        ),
    ]
