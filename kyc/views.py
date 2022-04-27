from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.
from service.models import Vehicle


def index(request: WSGIRequest) -> HttpResponse | Http404:
    """
    Homepage view
    Returns the homepage of the system
    """

    return render(request, 'kyc/index.html')
