from django.db import models
from apps.body_configuration.models import BodyPart
# Create your models here.
class Size(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20, null=True)
    gender = models.TextField(max_length=50, null=True)
    description = models.TextField(max_length=50, null=True)
    status = models.BooleanField(null=True)
    body_area = models.ForeignKey(BodyPart, null=True, blank=True, on_delete=models.SET_NULL)
