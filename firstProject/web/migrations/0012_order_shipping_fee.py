# Generated by Django 4.1.2 on 2022-12-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_shippingaddress_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_fee',
            field=models.FloatField(default=4.0),
        ),
    ]
