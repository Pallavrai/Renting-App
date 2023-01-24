from rest_framework import generics,permissions,mixins
from .serializers import UserprofileSerializer
from .models import Userprofile
from django.contrib.auth.models import User

class CreateProfileView(generics.CreateAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=UserprofileSerializer
    permission_classes=[permissions.IsAuthenticated]

create_profile=CreateProfileView.as_view()

class UserProfileView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=UserprofileSerializer
    lookup_field='user'
    permission_classes=[permissions.IsAuthenticated]

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    


profile_operations=UserProfileView.as_view()

class UserProfileListView(generics.ListAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=UserprofileSerializer
    permission_classes=[permissions.IsAuthenticated,permissions.DjangoModelPermissions]

list_profiles=UserProfileListView.as_view()

