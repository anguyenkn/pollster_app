# Generated by Django 3.0.3 on 2020-02-07 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choise',
            new_name='Choice',
        ),
    ]