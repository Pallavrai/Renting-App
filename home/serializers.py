from home.models import available_room
from rest_framework import serializers

class AvailroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=available_room
        fields='__all__'
