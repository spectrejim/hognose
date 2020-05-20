from django.db import models
from datetime import datetime, timedelta
import time

# Create your models here.
class Scenario(models.Model):
    name = models.TextField(max_length=255)
    overlays = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return str(self.name.title())

class Product(models.Model):
    name = models.TextField(max_length=255)
    scenarios = models.TextField(max_length=255)
    maps = models.CharField(max_length=255,blank=True)
    overlays = models.CharField(max_length=255,blank=True)
    location = models.TextField(max_length=255)
    date = models.CharField(max_length=64)
    publisher = models.TextField(max_length=255)

    def __str__(self):
        return str(f"Rating: {self.rating}, User Ratings: {self.user_ratings_total}")


class Maps(models.Model):
    name = models.TextField(max_length=255)
    description = models.CharField(max_length=255,blank=True)
    source = models.CharField(max_length=255,blank=True)
    publisher = models.TextField(max_length=255)
    
    def __str__(self):
        return str(f"Author: {self.author_name}, Rating: {self.rating}")

class Overlays(models.Model):
    name = models.TextField(max_length=255)
    description = models.CharField(max_length=255,blank=True)
    source = models.CharField(max_length=255,blank=True)
    publisher = models.TextField(max_length=255)
    
    def __str__(self):
        return str(f"Author: {self.author_name}, Rating: {self.rating}")