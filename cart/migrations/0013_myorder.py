# Generated by Django 4.0.1 on 2022-02-03 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0012_alter_delivery_delivereddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.delivery')),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order')),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
