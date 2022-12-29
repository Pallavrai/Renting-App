from rest_framework import generics,permissions
from .serializers import UserprofileSerializer
from .models import Userprofile
from django.contrib.auth.models import User

class CreateProfileView(generics.CreateAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=UserprofileSerializer
    permission_classes=[permissions.IsAuthenticated]

create_profile=CreateProfileView.as_view()

class UserProfileView(generics.RetrieveAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=UserprofileSerializer
    lookup_field='user'
    permission_classes=[permissions.IsAuthenticated]

get_profile=UserProfileView.as_view()

class UserProfileUpdateView(generics.UpdateAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=UserprofileSerializer
    lookup_field='user'
    permission_classes=[permissions.IsAuthenticated]

edit_profile=UserProfileUpdateView.as_view()

