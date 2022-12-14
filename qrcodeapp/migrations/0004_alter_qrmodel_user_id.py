# Generated by Django 4.1.4 on 2022-12-14 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qrcodeapp', '0003_remove_qrmodel_user_qrmodel_url_qrmodel_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrmodel',
            name='user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
