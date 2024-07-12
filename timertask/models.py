from django.db import models
from django.utils import timezone
from datetime import timedelta, datetime


def default_start_time():
    return datetime.now().time()

def default_end_time():
    return (datetime.now() + timedelta(minutes=45)).time()

class Timer(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField(default=default_start_time)
    end_time = models.TimeField(default=default_end_time)
    notified = models.BooleanField(default=False)

    def __str__(self):
        return f"Timer {self.name} "
