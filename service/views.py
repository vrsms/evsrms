from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponse
from .models import Vehicle


# Create your views here.

def index(request: WSGIRequest) -> HttpResponse | Http404:
    """
    Homepage view
    Returns the homepage of the service app
    """
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    latest_vehicle_list = Vehicle.objects.order_by('-make')[:5]

    context = {
        'latest_vehicle_list': latest_vehicle_list,
    }
    return render(request, 'service/index.html', context)


def detail(request: WSGIRequest, vehicle_id: int) -> HttpResponse | Http404:
    """
    Vehicle details
    """
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'service/detail.html', {'vehicle': vehicle})
