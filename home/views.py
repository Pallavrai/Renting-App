from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    data={
        'name':"Pallav",
        'd':"hello",
    }
    return Response(data)