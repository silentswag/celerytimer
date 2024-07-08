# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Timer
from .tasks import check_timer_end

@receiver(post_save, sender=Timer)
def post_save_timer(sender, instance, created, **kwargs):
    if created:
        # Schedule the Celery task to check if the end time is reached
        check_timer_end.apply_async((instance.name,), eta=instance.end)
