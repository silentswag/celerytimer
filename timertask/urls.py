# timers/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('timers/', TimerListCreateView.as_view(), name='timer-list-create'),
    path('list/',TimerDetailView.as_view())
]
