# Generated by Django 4.1.3 on 2023-02-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_address_zip'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_e6a359_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customers',
        ),
    ]
