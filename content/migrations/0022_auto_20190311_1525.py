# Generated by Django 2.0.3 on 2019-03-11 12:25

from django.db import migrations, models
import django.utils.datetime_safe
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_errorlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='time_uploaded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='errorlog',
            name='time_logged',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.datetime_safe.datetime.now),
            preserve_default=False,
        ),
    ]
