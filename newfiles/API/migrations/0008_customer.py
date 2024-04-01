# Generated by Django 5.0.2 on 2024-03-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_village'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('aadhar_number', models.CharField(max_length=12, unique=True)),
            ],
        ),
    ]
