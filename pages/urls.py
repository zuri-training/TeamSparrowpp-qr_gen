from django.urls import path
from .views import homePage, dashboard, type 

urlpatterns = [
    path("", homePage, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path( "types/", type, name="type"),
]