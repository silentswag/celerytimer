# timers/tasks.py
from celery import shared_task
from django.utils.timezone import now
from .models import Timer
import win32api  # For Windows notifications (pywin32)
from django.utils import timezone

@shared_task
def check_timer_end(task_name):
        win32api.MessageBox(0,"Checking timer","Notification",0x00001000)
        try:
            timer = Timer.objects.first()
            curr=timezone.now().time()
            if curr >= timer.end_time:
                # Handle the timer end logic here
                win32api.MessageBox(0, f"Timer {timer.name} has ended!", "Notification", 0x00001000)
                # You can also update the timer state or notify users here
                timer.notified = True
                timer.delete()
        except:
             win32api.MessageBox(0,"tasks has failed")

"""@shared_task
def check_and_notify():
    # Fetch timers that have ended and haven't been notified
    timers = Timer.objects.filter(end_time__lte=now(), notified=False)
    for timer in timers:
        # Send a Windows notification
        win32api.MessageBox(0, f"Timer {timer.name} has ended!", "Notification", 0x00001000)
        # Mark the timer as notified
        timer.notified = True
        timer.delete()"""
