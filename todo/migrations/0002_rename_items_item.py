# Generated by Django 3.2.16 on 2022-12-02 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='items',
            new_name='Item',
        ),
    ]
