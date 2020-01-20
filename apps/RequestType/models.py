from django.db import models
from apps.configurations.models import Element_Type
# Create your models here.

class Request_Type(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField(max_length=50)
    detail = models.TextField(max_length=50)
    Status = models.TextField(max_length=50)
    element_type_id=models.ForeignKey(Element_Type,on_delete=models.Case)

    def __str__(self):
	    return self.name