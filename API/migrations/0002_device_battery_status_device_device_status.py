# Generated by Django 5.0.2 on 2024-02-09 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='battery_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='device',
            name='device_status',
            field=models.BooleanField(default=False),
        ),
    ]
