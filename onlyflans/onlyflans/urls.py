"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#urls.py
from django.contrib import admin
from django.urls import path, include
from web import views
#from . import views --> importa todas las views de todas las apps


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('acerca/', views.about, name="about"),
    path('bienvenido/', views.welcome, name="welcome"), 
    path('contacto/', views.contacto, name="contacto"),  
    path('contacto_exitoso/', views.contacto_exitoso, name="contacto_exitoso"),  
    path('login/', views.login, name="login"),  
]

