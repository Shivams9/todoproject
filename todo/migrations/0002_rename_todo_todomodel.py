# Generated by Django 4.0.4 on 2022-11-04 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todo',
            new_name='todoModel',
        ),
    ]