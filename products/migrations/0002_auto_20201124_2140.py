# Generated by Django 3.1.3 on 2020-11-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]