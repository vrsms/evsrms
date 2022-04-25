from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Vehicle


# Create your views here.

def index(request: WSGIRequest) -> HttpResponse | Http404:
    """
    Homepage view
    Returns the homepage of the service app
    """
    latest_vehicle_list = Vehicle.objects.order_by('-make')[:5]

    context = {
        'latest_vehicle_list': latest_vehicle_list,
    }
    return render(request, 'service/index.html', context)


def detail(request: WSGIRequest, vehicle_id: int) -> HttpResponse | Http404:
    """
    Vehicle details
    """
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_id)
    except Vehicle.DoesNotExist:
        raise Http404("Vehicle does not exist")
    return render(request, 'service/detail.html', {'vehicle': vehicle})
