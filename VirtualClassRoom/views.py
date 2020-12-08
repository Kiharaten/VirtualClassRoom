from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User

def index(request):
    # response = "view index data"
    return render(request, 'VirtualClassRoom/index.html', {'response' : response})
    return HttpResponse(response)

def login(request):
    # response = "login page"
    return render(request, 'VirtualClassRoom/login.html', {'response' : response})
