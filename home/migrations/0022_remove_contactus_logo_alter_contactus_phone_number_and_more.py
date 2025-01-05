# Generated by Django 5.1.4 on 2025-01-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_contactus_remove_footer_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='logo',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='phone_number',
            field=models.CharField(default=123, max_length=25, verbose_name='Phone Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
