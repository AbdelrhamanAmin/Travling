from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
# from experience.models import *
# from car_rental.models import *
# from lonely_planet.models import *
# from reservation.models import *
# Create your models here.
class customUser(AbstractUser):
   user_image = models.ImageField(upload_to='static/')
  
# class Profile(models.Model):
#     user = models.OneToOneField( customUser, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#    #  def __str__(self):
#    #      return f'{self.user.username} Profile'

#    #  def save(self):
#    #      super().save()

#    #      img = Image.open(self.image.path)

#    #      if img.height > 300 or img.width > 300:
#    #          output_size = (300, 300)
#    #          img.thumbnail(output_size)
#    #          img.save(self.image.path)   
