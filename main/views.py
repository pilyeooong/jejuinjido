from django.shortcuts import render
from django.utils import timezone
from place.models import Place, Congestion
import requests
import json


def index(request):

    places = Place.objects.all()
    congestions = Congestion.objects.all()

    for congestion in congestions:
        if congestion.expiration_at < timezone.now():
            congestion.delete()

    return render(request, 'main/index.html', {'places': places, 'congestions': congestions})
