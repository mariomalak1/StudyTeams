from django.shortcuts import render, redirect
from django.contrib.auth.models import User as django_user_model
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages

# Create your views here.

def login_function(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = user_name, password = password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, f"Hello {user.username}")
            try:
                return redirect(request.GET.get('next'))
            except:
                return redirect("home")
        else:
            messages.add_message(request, messages.ERROR, "You Not Are In System Yet, You Can Sign Up From Here")
            redirect("signup")
    return render(request, "users/login.html")

def logout_function(request):
    logout(request)
    return redirect("login")

def signup_function(request):
    pass