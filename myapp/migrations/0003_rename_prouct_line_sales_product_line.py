# Generated by Django 4.1.5 on 2023-06-14 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_sales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='prouct_line',
            new_name='product_line',
        ),
    ]
