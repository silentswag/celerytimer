# Generated by Django 5.0.4 on 2024-07-08 09:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timertask', '0002_timer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timer',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
