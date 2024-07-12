# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Timer
from .tasks import check_timer_end
#from django.utils import timezone
import win32api
from datetime import datetime

@receiver(post_save, sender=Timer)
def post_save_timer(sender, instance, created, **kwargs):
    if created:
        win32api.MessageBox(0, "post_save signal triggered", "Debug Info", 0x00001000)
        current_date = datetime.now().date()
        end_time = instance.end_time
        end_datetime = datetime.combine(current_date, end_time)
        win32api.MessageBox(0, f"Scheduling task for: {end_datetime}", "Debug Info", 0x00001000)
        check_timer_end.apply_async((instance.name,), eta=end_datetime)
      