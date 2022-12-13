from django.urls import path
from .views import homePage, dashboard, generateQRcode

urlpatterns = [
    path("", homePage, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("qrcode/generate/", generateQRcode, name="generate-qrcode"),
]