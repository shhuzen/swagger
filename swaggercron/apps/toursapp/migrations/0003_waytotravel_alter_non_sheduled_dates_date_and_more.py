# Generated by Django 5.0.1 on 2024-01-16 22:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursapp', '0002_location_non_sheduled_dates_picture_week_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WayToTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='non_sheduled_dates',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='non_sheduled_dates',
            name='from_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='non_sheduled_dates',
            name='to_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='from_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='to_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='tourmodel',
            name='way_to_travel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='toursapp.waytotravel'),
        ),
    ]
