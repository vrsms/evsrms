from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.


def index(request: WSGIRequest) -> HttpResponse | Http404:
    """
    Homepage view
    Returns the homepage of the system
    """

    return render(request, 'kyc/index.html')
