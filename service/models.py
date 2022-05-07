from django.db import models


# Create your models here.
from kyc.models import Vehicle


class ServiceTicket(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    status = models.CharField('Operation status', max_length=30)
    item_serviced = models.CharField(max_length=30)
    frequency = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self):
        return self.item_serviced
