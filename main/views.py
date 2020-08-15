from django.shortcuts import render
from place.models import Place
import requests
import json


def index(request):

    places = Place.objects.all()

    return render(request, 'main/index.html', { 'places': places })
