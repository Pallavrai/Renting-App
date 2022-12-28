from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.rooms_list,name='RoomsList'),
    path('create/', views.create_ad,name='Create_ad')

]