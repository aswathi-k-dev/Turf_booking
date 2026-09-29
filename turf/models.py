from django.db import models

# Create your models here.

class Turf(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length = 200)
    phone = models.CharField(max_length=200)
    fee = models.IntegerField()

    def __str__(self):
        return self.name