from django.db import models
from django.contrib.auth.models import User
import os

current_status=[
    ('N','None'),
    ('P','Processing'),
    ('C','Completed')
    ]

def get_coordinate():
    return {'latitude':0,'longitude':0}

def get_uid(self,instance):
    return os.path.join('/',instance.available_room.owner_id)

class available_room(models.Model):
    owner_id=models.ForeignKey(User,on_delete=models.CASCADE)
    room_pic=models.ImageField(upload_to=get_uid,null=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    visits=models.IntegerField()
    current_members=models.CharField(max_length=25,null=True)
    rooms=models.IntegerField()
    Price=models.IntegerField()
    location=models.JSONField(default=get_coordinate)
    payment_status=models.CharField(max_length=25,choices=current_status,default=current_status[0][0])
    transaction=models.CharField(max_length=255,blank=True)



    def __str__(self):
        return str(self.title)