from django.db import models


# Create your models here.
class CustomUser(models.Model):
    cd = models.CharField(max_length=200)
    cddd = models.CharField(max_length=250)
