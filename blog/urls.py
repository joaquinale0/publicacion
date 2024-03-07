from django.urls import path
from .views import *
# from . import views

urlpatterns = [
    path("", InicioBlog.as_view() ,name="inicio"),
    path("CrearPoster/", CrearPosterVista.as_view(), name="crearPoster")
]
