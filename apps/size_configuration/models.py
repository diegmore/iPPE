from django.db import models
from apps.body_configuration.models import BodyPart
# Create your models here.
class Size(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

class Body_Size(models.Model):
    gender = models.TextField(max_length=50)
    description = models.TextField(max_length=50)
    status = models.BooleanField(null=True)
    body_area = models.ForeignKey(BodyPart, null=True, blank=True, on_delete=models.SET_NULL)
    size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.SET_NULL)