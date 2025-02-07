# Generated by Django 5.0.6 on 2024-07-13 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0005_networkobject_products_alter_product_provider"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="networkobject",
            name="products",
        ),
        migrations.AlterField(
            model_name="product",
            name="provider",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="network.networkobject",
                verbose_name="Поставщик",
            ),
        ),
    ]
