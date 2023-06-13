from django.urls import path
from . import views
########

urlpatterns = [
    path("", views.home, name="home"),
    path("topics/", views.all_topics_view, name="topics"),
    path("create_room/", views.create_room, name="create_room"),
    path("all_topics_json/", views.all_topics_json, name="all_topics_json"),
]
