# Generated by Django 4.1.5 on 2023-04-05 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_order_orders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderDetails',
        ),
    ]
