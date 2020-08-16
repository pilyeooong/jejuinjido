from django.urls import path
from . import views

app_name = 'place'

urlpatterns = [
    path('<int:placeId>/congestion/<int:value>/', views.add_congestion, name='add-congestion'),
]
