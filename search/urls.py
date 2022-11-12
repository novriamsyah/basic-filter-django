from .views import *
from django.urls import path

urlpatterns = [
    path('', Home),
    path('api/get_hotel/', get_hotel)
]