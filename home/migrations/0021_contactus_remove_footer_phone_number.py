# Generated by Django 5.1.4 on 2025-01-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_footer_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Site Logo')),
                ('title', models.CharField(max_length=100, verbose_name='Site Title')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
            ],
        ),
        migrations.RemoveField(
            model_name='footer',
            name='phone_number',
        ),
    ]
