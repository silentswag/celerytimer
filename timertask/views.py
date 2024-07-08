from django.shortcuts import render

# Create your views here.
# timers/views.py
from rest_framework import generics
from .models import Timer
from .serializers import TimerSerializer

class TimerListCreateView(generics.ListCreateAPIView):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer

class TimerDetailView(generics.ListAPIView):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
