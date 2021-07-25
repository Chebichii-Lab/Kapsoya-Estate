from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#class Neighbourhood
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=200)
    neighbourhood_location = models.CharField(max_length=200)
    neighbourhood_description = models.TextField(max_length=500, blank=True)
    neighbourhood_photo = CloudinaryField('photo', default='photo')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return self.neighbourhood_name

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

    def update_hood(self):
        neighbourhood_name = self.neighbourhood_name
        self.neighbourhood_name = neighbourhood_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.IntegerField(default=0)
    email = models.CharField(max_length=30, blank=True)
    profile_picture = CloudinaryField('profile')
    bio = models.TextField(max_length=500, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)
