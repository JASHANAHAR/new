# Generated by Django 5.1.4 on 2025-01-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_userdata_image_alter_userdata_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='name',
            field=models.CharField(default='Anonymus', max_length=50),
        ),
    ]
