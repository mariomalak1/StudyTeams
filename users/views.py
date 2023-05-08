from django.shortcuts import render
from django.contrib.auth.models import User as django_user_model
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import LoginForm
# Create your views here.

def login_function(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data.get("username"),
                password = form.cleaned_data.get("password"),
            )
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f"Hello {user.username}")
            else:
                messages.add_message(request, messages.ERROR, "You Not Are In System Yet")
    else:
        form = LoginForm()
    context = {"form":form}
    return render(request, "users/login.html", context)