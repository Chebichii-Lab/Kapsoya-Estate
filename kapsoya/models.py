from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

#class Neighbourhood
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=60,blank=False)
    neighbourhood_location = models.CharField(max_length=60,blank=False)
    occupants_count = models.IntegerField(null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighbour')
    neighbourhood_picture = CloudinaryField('image')

    def __str__(self):
        return f'{self.neighbourhood_name}neighbour'

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)

    @classmethod
    def update_occupants(cls,neighbourhood_id):
        occupant = cls.objects.get(id=neighbourhood_id)
        new_count = occupant.occupants_count + 1
        cls.objects.filter(id = neighbourhood_id).update(occupants_count = new_count)

    def update_neighbourhood(self):
        name = self.neighbourhood_name
        self.neighbourhood_name = name

#class User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='members', blank=True, null=True)
    neighbourhood_name = models.CharField(max_length=60,blank=False)
    location = models.CharField(max_length=60,blank=False)
    bio = models.TextField()
    profile_picture = CloudinaryField('image')
    neighbourhood_description = models.TextField()

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


#class Business
class Business(models.Model):
    business_name = models.CharField(max_length=100,blank=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='business_owner')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business', blank=True, null=True)
    business_email = models.CharField(max_length=150,blank=False)

    def __str__(self):
        return f'{self.business_name}business'

    def save_business(self):
        self.save()

    def create_business(self):
            self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = cls.objects.get(id = business_id)
        return business

    def update_business(self):
        name = self.business_name
        self.business_name = name

