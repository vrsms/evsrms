from django.shortcuts import render

from .models import Vehicle


# Create your views here.

def index(request):
    """
    Homepage view
    Returns the homepage of the service app
    """
    latest_vehicle_list = Vehicle.objects.order_by('-make')[:5]

    context = {
        'latest_vehicle_list': latest_vehicle_list,
    }
    return render(request, 'service/index.html', context)
