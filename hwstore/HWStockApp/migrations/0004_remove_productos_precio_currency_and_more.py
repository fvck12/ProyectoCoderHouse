# Generated by Django 4.1 on 2022-08-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HWStockApp', '0003_alter_productos_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='precio_currency',
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
