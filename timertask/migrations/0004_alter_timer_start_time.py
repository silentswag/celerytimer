# Generated by Django 5.0.4 on 2024-07-08 10:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timertask', '0003_alter_timer_end_time_alter_timer_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]