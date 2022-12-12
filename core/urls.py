"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from django.contrib.auth import views as auth_views
#from django.conf.urls.static import static
#from django.conf import settings


from accounts.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
	must_authenticate_view,
)

urlpatterns = [
    # Admin url
    path('admin/', admin.site.urls),
     #path('account/', account_view, name="account"),
      #path('login/', login_view, name="login"),
       path('accounts/signup', registration_view, name="signup"),
    # Accounts url
    path("accounts/", include("allauth.urls")),
    # Pages url
    path("", include("pages.urls")),
]
