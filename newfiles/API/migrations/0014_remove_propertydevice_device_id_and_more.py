# Generated by Django 5.0.2 on 2024-03-12 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0013_propertydevice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertydevice',
            name='device_id',
        ),
        migrations.RemoveField(
            model_name='propertydevice',
            name='geolocation_id',
        ),
        migrations.CreateModel(
            name='PropertyDeviceDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.device')),
                ('geolocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.geolocation')),
                ('property_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.propertydevice')),
            ],
        ),
        migrations.AddField(
            model_name='propertydevice',
            name='devices',
            field=models.ManyToManyField(through='API.PropertyDeviceDevice', to='API.device'),
        ),
    ]
