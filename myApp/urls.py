from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("",views.index,name='home'),
    path("info",views.about,name='about us'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact')
]