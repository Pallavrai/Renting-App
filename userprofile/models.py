from django.db import models
from django.contrib.auth.models import User
import os

def get_uid(instance,fname):
    return os.path.join(str(instance.user.id)+'/profile',fname)


class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to=get_uid,null=True)
    bio=models.CharField(max_length=255)
      
    def __str__(self) -> str:
        return str(self.user)
