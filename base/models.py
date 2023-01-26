from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)
    createdDateTime = models.DateTimeField(auto_now_add=True)
    updatedDateTime = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE, null = True) 


class Message(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    createdTime = models.DateTimeField(auto_now_add=True)    
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.content[0:7]
    

