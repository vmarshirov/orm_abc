# Generated by Django 4.1.7 on 2023-03-26 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_abc_app', '0011_alter_abc_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abc',
            options={'ordering': ('-a', 'id'), 'verbose_name': 'A_B_C', 'verbose_name_plural': 'A_B_C_S'},
        ),
    ]
