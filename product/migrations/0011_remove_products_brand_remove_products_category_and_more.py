# Generated by Django 4.0.5 on 2022-07-25 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_products_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='favorite',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
