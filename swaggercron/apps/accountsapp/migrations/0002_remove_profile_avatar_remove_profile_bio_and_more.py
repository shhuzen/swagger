# Generated by Django 5.0.1 on 2024-01-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='detailed_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='short_desription',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
