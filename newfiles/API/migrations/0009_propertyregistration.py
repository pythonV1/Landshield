# Generated by Django 5.0.2 on 2024-03-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.CharField(max_length=100, unique=True)),
                ('property_name', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('taluk', models.CharField(max_length=100)),
                ('survey_number', models.CharField(max_length=100)),
                ('survey_sub_division', models.CharField(max_length=100)),
                ('patta_number', models.CharField(max_length=100)),
                ('area', models.FloatField()),
                ('fmb', models.FileField(upload_to='fmb_pdfs')),
            ],
        ),
    ]