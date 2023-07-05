
from django.contrib import admin
from django.urls import path,include
from .views import Scrapping_request


urlpatterns = [
    path('request',Scrapping_request.as_view()),

]
