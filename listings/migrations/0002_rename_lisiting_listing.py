# Generated by Django 3.2.5 on 2021-08-05 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lisiting',
            new_name='Listing',
        ),
    ]
