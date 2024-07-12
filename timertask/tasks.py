# tasks.py
from celery import shared_task
#from django.utils import timezone
from .models import Timer
from datetime import datetime
import win32api  # For Windows notifications (pywin32)

from django.utils import timezone

import logging
from datetime import datetime
from celery import shared_task
from .models import Timer
from django.utils import timezone

logger = logging.getLogger(__name__)

@shared_task
def check_timer_end(task_name):
    try:
        timer = Timer.objects.get(name=task_name)
        current_time = datetime.now().time()

        print(f"Current time: {current_time}, Timer end time: {timer.end_time}")

        if current_time >= timer.end_time and not timer.notified:
            print(f"Timer {timer.name} has ended!")
            # Notify and update the timer's state
            timer.notified = True
            timer.save()
        else:
            print("Timer has not ended or already notified.")
    except Timer.DoesNotExist:
        print(f"Timer {task_name} does not exist!")
    except Exception as e:
        print(f"Error: {e}")


@shared_task
def check_all_timers():
    try:
        current_time = datetime.now().time()
        win32api.MessageBox(0, f"Checking all timers at {current_time}", "Debug Info", 0x00001000)
        
        timers = Timer.objects.filter(end_time__lte=current_time, notified=False)

        for timer in timers:
            win32api.MessageBox(0, f"Timer {timer.name} has ended!", "Notification", 0x00001000)
            timer.notified = True
            timer.save()
            win32api.MessageBox(0, f"Timer {timer.name} notified state updated and saved.", "Debug Info", 0x00001000)
    except Exception as e:
        win32api.MessageBox(0, f"Error: {e}", "Notification", 0x00001000)

"""@shared_task
def check_timer_end(task_name):
    try:
        # Try to retrieve the Timer object by name
        timer = Timer.objects.get(name=task_name)
        current_time = datetime.now().time()
        #formatted_time = current_time.strftime("%H:%M:%S")

        # Debug: Print current time and end time
        win32api.MessageBox(0, f"Current time: {current_time}\nTimer end time: {timer.end_time}", "Debug Info", 0x00001000)

        if current_time >= timer.end_time and not timer.notified:
            # Notify that the timer has ended
            win32api.MessageBox(0, f"Timer {timer.name} has ended!", "Notification", 0x00001000)
            
            # Update the timer's notified state
            timer.notified = True
            timer.delete()

            # Debug: Confirmation message after saving
            win32api.MessageBox(0, "Timer notified state updated and saved.", "Debug Info", 0x00001000)
        else:
            # Debug: Reason for no notification
            if current_time < timer.end_time:
                win32api.MessageBox(0, "Current time is less than the end time.", "Debug Info", 0x00001000)
            elif timer.notified:
                win32api.MessageBox(0, "Timer has already been notified.", "Debug Info", 0x00001000)
    except Timer.DoesNotExist:
        win32api.MessageBox(0, f"Timer {task_name} does not exist!", "Notification", 0x00001000)
    except Exception as e:
        win32api.MessageBox(0, f"Error: {e}", "Notification", 0x00001000)"""
