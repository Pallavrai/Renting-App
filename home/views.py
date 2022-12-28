from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.serializers import AvailroomsSerializer
from home.models import available_room
from rest_framework import generics


class RoomslistView(generics.ListAPIView):
    queryset=available_room.objects.all()
    serializer_class=AvailroomsSerializer

rooms_list=RoomslistView.as_view()

class CreateAdView(generics.CreateAPIView):
    queryset=available_room.objects.all()
    serializer_class=AvailroomsSerializer

publish_ad=CreateAdView.as_view()
