from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# @login_required
def home(request):
    messages.add_message(request, messages.SUCCESS, "my message")
    return render(request, "base\home.html")