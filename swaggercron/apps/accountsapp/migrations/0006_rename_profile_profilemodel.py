# Generated by Django 5.0.1 on 2024-01-18 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0005_alter_profile_picture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfileModel',
        ),
    ]