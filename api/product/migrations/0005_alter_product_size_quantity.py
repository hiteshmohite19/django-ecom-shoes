# Generated by Django 5.0 on 2024-03-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_size_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size_quantity',
            field=models.JSONField(),
        ),
    ]