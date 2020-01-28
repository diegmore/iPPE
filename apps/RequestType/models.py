from django.db import models
from apps.configurations.models import Element_Type


class Request_Type(models.Model):
    code = models.CharField(unique=True, max_length=10)
    name = models.TextField(max_length=50, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    status = models.TextField(max_length=50, null=True, blank=True)
    element_type = models.ForeignKey(Element_Type ,null=True,blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
	    return self.name



