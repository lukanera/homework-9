# Generated by Django 5.1.3 on 2024-12-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_price_product_raiting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=1000, default=0, max_digits=10000),
        ),
    ]