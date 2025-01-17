# Generated by Django 3.2.25 on 2024-12-16 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_grp_imagefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('originalfilename', models.CharField(max_length=250)),
                ('GROUP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.grp')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='GroupDocumentHash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashvalue', models.CharField(max_length=100)),
                ('GROUPDOCUMENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.groupdocument')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
