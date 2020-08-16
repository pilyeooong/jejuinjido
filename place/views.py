import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Congestion, Place


def place_detail(request, placeId):
    pass


def add_congestion(request, placeId, value):
    place = get_object_or_404(Place, id=placeId)

    # value 혼잡도 값은 1~3만 받아온다
    # 직접 url 입력하여 접근하려 할 시에 리다이렉트
    if not 1 <= int(value) <= 3:
        return redirect('/')

    Congestion.objects.create(value=value, place=place, expiration_at=timezone.now(
    ) + datetime.timedelta(hours=6))

    return redirect('/')
