# Generated by Django 5.1.4 on 2025-01-03 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_footerlink_footer_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='links',
        ),
        migrations.AddField(
            model_name='footer',
            name='links',
            field=models.ForeignKey(blank=True, default=23, on_delete=django.db.models.deletion.CASCADE, to='home.footerlink'),
            preserve_default=False,
        ),
    ]
