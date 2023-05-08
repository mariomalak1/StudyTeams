from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

@login_required
def home(request):
    return render(request, "base\home.html")

@login_required
def notHome(request):
    return HttpResponse("<h1>mario</h1>")