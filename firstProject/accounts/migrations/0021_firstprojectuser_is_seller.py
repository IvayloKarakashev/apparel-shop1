# Generated by Django 3.2.17 on 2023-03-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_remove_firstprojectuser_is_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstprojectuser',
            name='is_seller',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
