# Generated by Django 5.0.6 on 2024-07-14 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0014_alter_networkobject_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="networkobject",
            options={
                "ordering": ["town"],
                "verbose_name": "Объект сети",
                "verbose_name_plural": "Объекты сети",
            },
        ),
    ]