# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("you can login from here.")

def join(request):
    return HttpResponse("you can join classroom from here.")

def archive(request):
    return HttpResponse("you can see archive from here.")

def mypage(request):
    return HttpResponse("you can check mypage here.")
