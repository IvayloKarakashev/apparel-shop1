# Generated by Django 4.1.2 on 2022-12-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_firstprojectuser_is_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstprojectuser',
            name='is_seller',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Seller', 'Seller')], max_length=50),
        ),
    ]
