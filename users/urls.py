from django.urls import path
# from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
   path("login/", views.login_function, name="login"),
   path("logout/", views.logout_function, name="logout"),
   path("signup/", views.signup_function, name="signup"),
]