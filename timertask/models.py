from django.db import models
from datetime import timedelta,datetime


class Timer(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField(default=datetime.now())  # Default to current time
    end_time = models.TimeField(default=(datetime.now()+timedelta(minutes=45)))
    notified = models.BooleanField(default=False)


    def __str__(self):
        return f"Timer {self.name} "
