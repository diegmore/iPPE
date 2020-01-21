from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.TextField(max_length=20, null=True)

    def __str__(self):
	    return self.name

class Stockits(models.Model):
    name = models.TextField(max_length=20, null=True)
    position = models.CharField(max_length=20, null=True)
    grant_input = models.BooleanField(null=True)
    grant_output = models.BooleanField(null=True)

    
class Warehouse(models.Model):
    name = models.CharField(max_length=20, null=True)
    addres = models.TextField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)
    stockists = models.ForeignKey(Stockits, null=True, blank=True, on_delete=models.SET_NULL)