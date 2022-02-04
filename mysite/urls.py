from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
 path("",views.index,name='home'),
 path("press", views.press, name="press"),
 path("about", views.about, name="about"),
 path("contact", views.contact, name="contact"),

]