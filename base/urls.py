from django.urls import path
from . import views
########

urlpatterns = [
    path("", views.home, name="home"),
    path("notHome/", views.notHome, name="notHome"),
]
