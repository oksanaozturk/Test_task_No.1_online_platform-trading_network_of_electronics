# Generated by Django 5.0.6 on 2024-07-12 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="networkobject",
            name="products",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="network.product",
                verbose_name="Продукты",
            ),
        ),
    ]
