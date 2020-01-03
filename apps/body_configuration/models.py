from django.db import models

# Create your models here.
class BodyPart(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=50)
    status = models.BooleanField(null=True)
    create_date = models.DateField(blank=True, null=True, auto_now=True)
