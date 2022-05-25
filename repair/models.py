import random
import string
from django.db import models
from service.models import Vehicle

# Create your models here.
reference_string = string.ascii_letters + string.digits + string.punctuation


class Ticket(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    ref = models.CharField('Reference', default=''.join(random.sample(reference_string, 10)), max_length=50)
    status = models.CharField('Operation status', max_length=30)
    item_maintained = models.CharField(max_length=30)
    frequency = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self):
        return self.ref
