# Generated by Django 5.1.4 on 2025-01-14 11:50

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_userdata_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='country',
            field=django_countries.fields.CountryField(default='India', max_length=50),
        ),
    ]
