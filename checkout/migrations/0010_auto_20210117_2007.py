# Generated by Django 3.1.3 on 2021-01-17 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20210110_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='zipcode',
            new_name='postal_code',
        ),
    ]
