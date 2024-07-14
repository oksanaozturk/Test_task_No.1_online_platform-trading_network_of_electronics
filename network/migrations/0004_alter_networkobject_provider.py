# Generated by Django 5.0.6 on 2024-07-13 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0003_remove_networkobject_products_product_provider"),
    ]

    operations = [
        migrations.AlterField(
            model_name="networkobject",
            name="provider",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите поставщика",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="network.networkobject",
                verbose_name="Поставщик",
            ),
        ),
    ]