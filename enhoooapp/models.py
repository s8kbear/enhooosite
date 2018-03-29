from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(null=True, blank=True, max_length=30)
    location = models.CharField(null=True, blank=True, max_length=150)
    postcode = models.CharField(null=True, blank=True, max_length=7)
    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(null=True, blank=True, max_length=30)
    def __str__(self):
        return self.name
