# Generated by Django 5.0.10 on 2025-01-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, default='Untitled', max_length=255),
        ),
    ]
