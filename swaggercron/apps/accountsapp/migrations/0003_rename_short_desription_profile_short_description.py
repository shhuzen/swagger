# Generated by Django 5.0.1 on 2024-01-16 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0002_remove_profile_avatar_remove_profile_bio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='short_desription',
            new_name='short_description',
        ),
    ]
