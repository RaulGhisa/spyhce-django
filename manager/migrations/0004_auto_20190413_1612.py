# Generated by Django 2.2 on 2019-04-13 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20190413_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.Board'),
            preserve_default=False,
        ),
    ]
