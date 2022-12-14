from django.urls import path
from .views import homePage, dashboard, types

urlpatterns = [
    path("", homePage, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path( "types/", types, name="types"),
]