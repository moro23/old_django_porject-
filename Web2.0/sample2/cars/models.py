from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.TextField()
    license = models.TextField()

class Car(models.Model):
    name = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    vin = models.TextField()
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
