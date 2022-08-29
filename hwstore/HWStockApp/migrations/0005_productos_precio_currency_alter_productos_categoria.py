# Generated by Django 4.1 on 2022-08-29 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HWStockApp', '0004_remove_productos_precio_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='precio_currency',
            field=models.CharField(default=11, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productos',
            name='categoria',
            field=models.CharField(blank=True, choices=[('C', 'Construccion'), ('P', 'Pintura'), ('B', 'Baños'), ('M', 'Madera'), ('H', 'Hogar'), ('J', 'Jardin'), ('E', 'Electricidad'), ('O', 'Otros')], max_length=1),
        ),
    ]
