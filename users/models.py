from django.db import models


# Create your models here.
class CustomUser(models.Model):
    cd = models.CharField(max_length=200)
    cddd = models.CharField(max_length=250)
    new = models.CharField(max_length=150)
    new = models.IntegerField()
    merge_new = models.CharField(max_length=150)
