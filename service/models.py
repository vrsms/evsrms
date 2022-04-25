from django.db import models


# Create your models here.

class Vehicle(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField('vehicle_model', max_length=20)

    def __str__(self):
        return self.make


class ServiceTicket(models.Model):
    service_ticket = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service_date = models.DateTimeField('ServiceTicket Date')
    cost = models.IntegerField(default=0)
