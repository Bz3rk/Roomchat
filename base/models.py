from django.db import models

from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.




class Avatar(models.Model):
    image = models.ImageField( upload_to='images/' )


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    avatar = models.ForeignKey(Avatar,on_delete=models.SET_DEFAULT, default="10", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Topic(models.Model):
    name = models.CharField(max_length=250, unique=True)
    

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    members =  models.ManyToManyField(User, related_name='members', blank=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']
    


    def __str__(self):
        return self.name
    
    

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['-updated', '-created']
    

    def __str__ (self):
        return self.body[0:20]
    
