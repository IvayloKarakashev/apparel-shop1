# Generated by Django 4.1.2 on 2022-12-10 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_order_shipping_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 12, 10, 12, 21, 22, 204255, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
