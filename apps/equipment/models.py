from django.db import models

from apps.configurations.models import Element_Classification
from apps.body_configuration.models import BodyPart
# Create your models here.
class Work_Activities(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(max_length=50, null=True)
    def __str__(self):
	    return self.name


class Equipment (models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20, null=True)
    time_of_life = models.TextField(max_length=50, null=True)
    manteinance_cleaning = models.TextField(max_length=50, null=True)
    description = models.TextField(max_length=50, null=True)
    certification = models.TextField(max_length=50, null=True)
    mode_use = models.TextField(max_length=50, null=True)
    status = models.BooleanField(null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    body_area = models.ForeignKey(BodyPart, null=True, blank=True, on_delete=models.SET_NULL)
    element_classification = models.ForeignKey(Element_Classification, null=True, blank=True, on_delete=models.SET_NULL)
    work_activities = models.ManyToManyField(Work_Activities, blank=True)
    
class Protection_Barrier(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(max_length=50, null=True)