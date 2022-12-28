from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.rooms_list,name='RoomsList'),
    path('publish/', views.publish_ad,name='publish_ad')

]