# Generated by Django 4.1.2 on 2022-12-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_orderitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='label',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
