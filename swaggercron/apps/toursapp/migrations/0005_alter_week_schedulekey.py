# Generated by Django 5.0.1 on 2024-01-17 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursapp', '0004_remove_schedule_non_sheduled_dates_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='schedulekey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='toursapp.schedule'),
        ),
    ]
