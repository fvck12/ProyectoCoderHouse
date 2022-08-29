# Generated by Django 4.1 on 2022-08-28 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HRApp', '0003_alter_empleado_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='user_id',
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(default=111, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
