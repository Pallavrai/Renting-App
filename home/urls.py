from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.rooms_list,name='RoomsList'),
    path('auth/', obtain_auth_token),
    path('publish/', views.publish_ad,name='publish_ad'),
    path('update/<int:pk>/',views.update_ad,name='update_ad')

]