# Generated by Django 5.1.4 on 2025-01-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_footer_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
