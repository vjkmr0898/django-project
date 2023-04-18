# Generated by Django 4.1.5 on 2023-04-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=45)),
                ('uom', models.CharField(max_length=45)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_items', models.IntegerField()),
                ('to_sale', models.CharField(default='YES', max_length=45)),
            ],
        ),
    ]
