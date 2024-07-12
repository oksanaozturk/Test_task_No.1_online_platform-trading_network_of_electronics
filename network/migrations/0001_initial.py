# Generated by Django 5.0.6 on 2024-07-12 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название продукта', max_length=150, verbose_name='Название продукта')),
                ('model', models.CharField(blank=True, help_text='Введите модель продукта', max_length=150, null=True, verbose_name='Модель продукта')),
                ('launch_date', models.DateField(auto_now_add=True, help_text='Введите дату выхода продукта на рынок', verbose_name='Дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='NetworkObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название объекта сети', max_length=100, verbose_name='Название объекта сети')),
                ('email', models.EmailField(blank=True, help_text='Введите email', max_length=254, null=True, verbose_name='Email')),
                ('country', models.CharField(blank=True, help_text='Введите назание страны', max_length=50, null=True, verbose_name='Страна')),
                ('town', models.CharField(blank=True, help_text='Введите назание города', max_length=50, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, help_text='Введите назание улицы', max_length=100, null=True, verbose_name='Улица')),
                ('house', models.PositiveIntegerField(blank=True, help_text='Введите номер дома', null=True, verbose_name='Номер дома')),
                ('debt_to_provider', models.DecimalField(blank=True, decimal_places=2, help_text='Введите долг перел Поставщиком', max_digits=10, null=True, verbose_name='Долг перед поставщиком')),
                ('time_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('provider', models.ForeignKey(help_text='Укажите поставщика', on_delete=django.db.models.deletion.CASCADE, to='network.networkobject', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Объект сети',
                'verbose_name_plural': 'Объекты сети',
            },
        ),
    ]