# Generated by Django 5.0 on 2024-03-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size_quantity',
            field=models.CharField(null=True),
        ),
    ]
