# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("you can login from here.")

def payment(request):
    return HttpResponse("you can check payment from here.")

def status(request):
    return HttpResponse("you can see status from here.")

def notice(request):
    return HttpResponse("you can check notice here.")