# Generated by Django 4.0.6 on 2022-08-08 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_members_base'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Base',
            new_name='Person',
        ),
    ]
