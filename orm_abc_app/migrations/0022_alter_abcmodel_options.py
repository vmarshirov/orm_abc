# Generated by Django 4.1.7 on 2024-04-06 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_abc_app', '0021_alter_abcmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abcmodel',
            options={'ordering': ('-pk',), 'verbose_name': 'A_B_C_Таблица', 'verbose_name_plural': 'A_B_C_Таблицы'},
        ),
    ]
