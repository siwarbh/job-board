from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE)
    phone_number = models.CharField(max_length = 15)
    image = models.ImageField(upload_to ='profile/')
    city = models.ForeignKey('city',related_name='user_city', on_delete=models.CASCADE, blank = True, null=True)
    
    
    def __str__(self):
        return str(self.user)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    
    
class city(models.Model): 
    name = models.CharField(max_length= 30)
    def __str__(self):
        return str(self.name)


