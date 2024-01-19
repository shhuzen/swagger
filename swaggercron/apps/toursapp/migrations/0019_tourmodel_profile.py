# Generated by Django 5.0.1 on 2024-01-19 02:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0007_profilemodel_user'),
        ('toursapp', '0018_rename_location_locationmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourmodel',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accountsapp.profilemodel'),
        ),
    ]
