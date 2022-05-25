from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponse
from .models import Suggestion


# Create your views here.

def index(request: WSGIRequest) -> HttpResponse | Http404:
    """
    Homepage view
    Returns the homepage of the suggestions app
    """
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    latest_suggestion_list = Suggestion.objects.order_by('-title')[:5]

    context = {
        'latest_vehicle_list': latest_suggestion_list,
    }
    return render(request, 'suggestions/index.html', context)


def detail(request: WSGIRequest, suggestion_id: int) -> HttpResponse | Http404:
    """
    Suggestion details
    """
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    return render(request, 'suggestions/detail.html', {'suggestion': suggestion})
