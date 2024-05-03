from django.db import models

# Create your models here.

class country(models.Model):
    state=models.CharField(max_length=25)
    city=models.CharField(max_length=25)
    postal_code=models.IntegerField()