# Generated by Django 3.2.25 on 2024-12-17 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_groupdocument_groupdocumenthash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupdocumenthash',
            name='hashvalue',
            field=models.CharField(max_length=1000),
        ),
    ]