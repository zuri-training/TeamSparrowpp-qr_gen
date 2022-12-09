from django.urls import path
from .views import homePage, dashboard

urlpatterns = [
    path("", homePage, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
]