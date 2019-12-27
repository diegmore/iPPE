from django.db import models

# Create your models here.


class Element_Type(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=50)
    def __str__(self):
	    return self.code

class Element_Classification(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=50)
    status = models.BooleanField(null=True)
    create_date = models.DateField(blank=True, null=True, auto_now=True)
    element_type = models.ForeignKey(Element_Type, null=True, blank=True, on_delete=models.SET_NULL)
