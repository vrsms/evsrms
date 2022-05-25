from django.db import models


# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField('vehicle_model', max_length=30)
    plate_number = models.CharField('Plate number', max_length=30)
    category = models.CharField(max_length=30)
    status = models.CharField('Operation status', max_length=30)

    def __str__(self):
        return self.plate_number
