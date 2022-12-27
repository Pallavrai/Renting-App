from django.db import models

class available_rooms(models.Model):
    owner_id=models.IntegerField()
    title=models.CharField(max_length=25)
    description=models.CharField(max_length=255)
    visits=models.IntegerField()
    current_members=models.CharField(max_length=25)
    rooms=models.IntegerField()
    Price=models.IntegerField()

    def __str__(self):
        return str(self.title)