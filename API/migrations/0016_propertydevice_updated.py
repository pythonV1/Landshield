# Generated by Django 5.0.2 on 2024-03-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0015_propertydevice_last_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydevice',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
