from django.db import models
from django.contrib.auth import get_user_model
user=get_user_model()


class Locations(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE, related_name='locations')
    longitude=models.FloatField()
    latitude=models.FloatField()
    timestamp= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user.email)
