# Generated by Django 3.2.17 on 2023-03-22 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': 'Shipping addresses'},
        ),
    ]
