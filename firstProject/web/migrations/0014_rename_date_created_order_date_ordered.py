# Generated by Django 4.1.2 on 2022-12-10 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_order_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_created',
            new_name='date_ordered',
        ),
    ]
