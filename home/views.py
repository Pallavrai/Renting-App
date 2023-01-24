from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.serializers import AvailroomsSerializer
from home.models import available_room
from .permissions import IsownerPermission
from rest_framework import generics,mixins,permissions,authentication


class RoomslistView(generics.ListAPIView):
    queryset=available_room.objects.all()
    serializer_class=AvailroomsSerializer

rooms_list=RoomslistView.as_view()

class CreateAdView(generics.CreateAPIView):
    queryset=available_room.objects.all()
    serializer_class=AvailroomsSerializer

publish_ad=CreateAdView.as_view()

class UpdateAdView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=available_room.objects.all()
    serializer_class=AvailroomsSerializer
    permission_classes=[permissions.IsAdminUser,permissions.IsAuthenticated,permissions.DjangoObjectPermissions,IsownerPermission]
    authentication_classes=[authentication.SessionAuthentication,authentication.TokenAuthentication]

    lookup_field='pk'

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request, *args, **kwargs)

update_ad=UpdateAdView.as_view()

