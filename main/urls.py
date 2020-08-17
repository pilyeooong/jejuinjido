from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category_name>/', views.place_in_category, name='place_in_category'),
]
