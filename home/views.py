from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.serializers import AvailroomsSerializer
from home.models import available_rooms

@api_view(['GET'])
def home(request):
    instance=available_rooms.objects.all()
    s=AvailroomsSerializer(instance,many=True).data
    return Response(s)