# Generated by Django 3.2.25 on 2024-12-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_grp_grpmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='grpmember',
            name='privatekey',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grpmember',
            name='publickey',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
