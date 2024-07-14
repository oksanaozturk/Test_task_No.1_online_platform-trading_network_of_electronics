# Generated by Django 5.0.6 on 2024-07-13 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0010_alter_networkobject_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="networkobject",
            options={
                "ordering": ["town"],
                "permissions": [
                    ("delete_debt_to_provider", "Can delete debt_to_provider")
                ],
                "verbose_name": "Объект сети",
                "verbose_name_plural": "Объекты сети",
            },
        ),
    ]