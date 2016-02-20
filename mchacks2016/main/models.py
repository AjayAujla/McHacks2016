from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=7)
    
class Preference(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    
class Availability(models.Model):
    