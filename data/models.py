from django.db import models

# Create your models here.

class Log(models.Model):
  id = models.AutoField(primary_key=True)
  time = models.DateTimeField(max_length=200)
  ip = models.CharField(max_length=200)
  user_agent = models.CharField(max_length=200)
  accept_language = models.CharField(max_length=200)
