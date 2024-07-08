# timers/serializers.py
from rest_framework import serializers
from .models import Timer

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = [ 'name','start_time', 'end_time', 'notified']
