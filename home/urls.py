from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("privacy", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("faq/", views.faq, name="faq"),
]
