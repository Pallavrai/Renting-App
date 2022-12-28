from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:user>/', views.get_profile,name='Get_profile'),
    path('create/',views.create_profile,name='Create_profile')
]
