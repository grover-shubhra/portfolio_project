# Generated by Django 2.2 on 2021-12-23 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20211223_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imageFullname',
            new_name='image',
        ),
    ]
