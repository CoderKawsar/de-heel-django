# Generated by Django 5.1.4 on 2025-01-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_directormessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='missionvision',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Title'),
        ),
    ]
