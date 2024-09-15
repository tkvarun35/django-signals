from django.db import models

# Create your models here.


class Message(models.Model):
    mess=models.CharField(max_length=100)