# Generated by Django 5.0.2 on 2024-02-29 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_devicetype_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]