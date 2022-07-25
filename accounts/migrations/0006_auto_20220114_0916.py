# Generated by Django 3.2.4 on 2022-01-14 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220114_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='default_User_Address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.default_user_address'),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='phone_verified',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]