# Generated by Django 3.2.20 on 2024-10-06 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='imagename',
            new_name='originalfilename',
        ),
    ]
