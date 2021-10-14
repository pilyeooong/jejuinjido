import datetime

from bs4 import BeautifulSoup
from urllib import parse

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

import time

from .models import Congestion, Place


def place_detail(request, placeId):
    place = get_object_or_404(Place, id=placeId)
    # print(place)
    # url = "https://www.instagram.com/explore/tags/{}/".format(place)

    # options = webdriver.ChromeOptions()

    # options.add_argument('headless')
    # options.add_argument('disable-gpu')
    # options.add_argument('lang=ko_KR')

    # driver = webdriver.Chrome('chromedriver', options=options)

    # driver.get(url)
    # time.sleep(3)

    # posts = []
    # images = driver.find_elements_by_css_selector('.Nnq7C img')

    # for img in images:
    #     post = img.get_attribute('src')
    #     posts.append(post)

    # posts = posts[10:14]
    # driver.close()

    return render(request, 'place/place_detail.html', {'place': place })


def add_congestion(request, placeId, value):
    place = get_object_or_404(Place, id=placeId)

    # value 혼잡도 값은 1~3만 받아온다
    # 직접 url 입력하여 접근하려 할 시에 리다이렉트
    if not 1 <= int(value) <= 3:
        return redirect('/')

    Congestion.objects.create(value=value, place=place, expiration_at=timezone.now(
    ) + datetime.timedelta(hours=6))

    return redirect('/')
