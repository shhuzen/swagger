# Generated by Django 5.0.1 on 2024-01-18 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('toursapp', '0018_rename_location_locationmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('open', 'open'), ('advance', 'advance'), ('paid', 'paid')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=9, max_digits=15)),
                ('advance_amount', models.DecimalField(decimal_places=9, max_digits=15)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phonenumber', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('adult_travelers_count', models.IntegerField()),
                ('child_travelers_count', models.IntegerField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toursapp.tourmodel')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
