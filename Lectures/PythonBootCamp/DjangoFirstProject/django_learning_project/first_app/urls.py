from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:item>/", views.courses, name="kurs"),
    path("<int:num1>/<int:num2>/", views.multiply_view, name="multiply"),
]
