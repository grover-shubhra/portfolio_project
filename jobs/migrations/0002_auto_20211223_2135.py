# Generated by Django 2.2 on 2021-12-23 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='imageFullname',
        ),
    ]