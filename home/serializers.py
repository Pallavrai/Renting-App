from home.models import available_rooms
from rest_framework import serializers

class AvailroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=available_rooms
        fields='__all__'
