# Generated by Django 5.0.1 on 2024-01-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0003_rename_short_desription_profile_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/pictures/'),
        ),
    ]
