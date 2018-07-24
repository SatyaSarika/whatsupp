from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    fromuser=models.IntegerField(default=0)
    touser=models.IntegerField(default=0)
    chattext = models.TextField("ChatBox",default=" ")