from django.apps import AppConfig


class TimertaskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'timertask'
    def ready(self):
        import timertask.signals
