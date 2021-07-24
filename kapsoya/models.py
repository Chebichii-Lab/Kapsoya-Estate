from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Neighbourhood
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=60,blank=False)
    neighbourhood_location = models.CharField(max_length=60,blank=False)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighbour')

#class User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='members', blank=True, null=True)
    neighbourhood_name = models.CharField(max_length=60,blank=False)
    location = models.CharField(max_length=60,blank=False)
    bio = models.TextField()
