# Generated by Django 4.2.5 on 2024-01-12 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_shippingaddress_address_ptr_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
