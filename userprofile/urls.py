from django.urls import path,include
from . import views

urlpatterns = [
    path('edit/<int:user>/', views.profile_operations,name='Profile_operations'),
    path('', views.list_profiles,name='Profile'),
    path('create/',views.create_profile,name='Create_profile'),
]
