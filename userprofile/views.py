from rest_framework import generics
from .serializers import UserprofileSerializer
from .models import Userprofile

class CreateProfileView(generics.CreateAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=UserprofileSerializer

create_profile=CreateProfileView.as_view()

class UserProfileView(generics.RetrieveAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=UserprofileSerializer
    lookup_field='user'
    

get_profile=UserProfileView.as_view()