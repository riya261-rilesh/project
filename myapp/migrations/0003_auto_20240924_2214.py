# Generated by Django 3.2.20 on 2024-09-24 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_news'),
    ]

    operations = [
        migrations.DeleteModel(
            name='news',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='LOGIN',
        ),
        migrations.DeleteModel(
            name='Reqstatus',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
