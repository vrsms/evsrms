from django.db import models


# Create your models here.
from service.models import Vehicle


class Suggestion(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField('description', max_length=30)

    def __str__(self):
        return self.title
