# Generated by Django 5.0.1 on 2024-01-17 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursapp', '0015_schedule_tourkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='tourkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='toursapp.tourmodel'),
        ),
    ]
