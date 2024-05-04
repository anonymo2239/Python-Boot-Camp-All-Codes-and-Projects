from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "template_app/first.html")

def weather_view(request):
    weather_dict = {
        "Istanbul" : 30,
        "Amsterdam" : 20,
        "Paris" : [5, 20, 4, 35],
        "Rome" : {"Morning" : 25, "Evening" : 15},
        "User_premium" : True
    }
    return render(request, "template_app/weather.html", context=weather_dict)