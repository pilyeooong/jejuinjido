from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from place.models import Place, Congestion, Category
import requests
import json


def index(request):

    places = Place.objects.all()
    congestions = Congestion.objects.all()
    categories = Category.objects.all()

    for congestion in congestions:
        if congestion.expiration_at < timezone.now():
            congestion.delete()

    return render(request, 'main/index.html', {'places': places, 'congestions': congestions, 'categories': categories})


def place_in_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    categories = Category.objects.all()
    places = Place.objects.filter(category=category)
    congestions = Congestion.objects.all()

    return render(request, 'main/index.html', {'places': places, 'categories': categories, 'congestions': congestions })

