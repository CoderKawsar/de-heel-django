# Generated by Django 5.1.4 on 2025-01-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_strength'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorylevel2',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Product Image'),
        ),
    ]
