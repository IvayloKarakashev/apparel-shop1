# Generated by Django 4.1.2 on 2022-12-23 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_firstprojectuser_is_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstprojectuser',
            name='is_seller',
        ),
    ]
