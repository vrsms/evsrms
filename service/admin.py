from django.contrib import admin
from .models import Vehicle
from .models import Service

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Service)
