from django.urls import path
from .views import signupPage, loginPage, logoutView
urlpatterns = [
    path("signup/", signupPage, name="signup"),
    path("login/", loginPage, name="login"),
    path("logout/", logoutView, name="logout")
]