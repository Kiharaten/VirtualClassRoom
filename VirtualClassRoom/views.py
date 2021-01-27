from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# from .models import User

response = {
    "title" : "",
    "h1" : "",
    "page_name": "",
}

def index(request):
    response["title"] = "VirtualClassRoom | welcome"
    response["h1"] = "view page index"
    
    return render(request, 'VirtualClassRoom/index.html', response)

def login(request):
    response["title"] = "VirtualClassRoom | login"
    response["h1"] = "login page"

    return render(request, 'VirtualClassRoom/login.html', response)

def mypage(request):      # removed user_id
    response["title"] = "VirtualClassRoom | mypage"
    response["h1"] = "test_user1"

    return render(request, 'VirtualClassRoom/mypage.html', response)

def A(request):
    response["title"] = "VirtualClassRoom | mypage"
    response["h1"] = "test_user1"
    response["page_name"] = "pageA"

    return render(request, 'VirtualClassRoom/mypage.html', response)

def B(request):
    response["title"] = "VirtualClassRoom | mypage"
    response["h1"] = "test_user1"
    response["page_name"] = "pageB"

    return render(request, 'VirtualClassRoom/mypage.html', response)

def C(request):
    response["title"] = "VirtualClassRoom | mypage"
    response["h1"] = "test_user1"
    response["page_name"] = "pageC"

    return render(request, 'VirtualClassRoom/mypage.html', response)

def D(request):
    response["title"] = "VirtualClassRoom | mypage"
    response["h1"] = "test_user1"
    response["page_name"] = "pageD"

    return render(request, 'VirtualClassRoom/mypage.html', response)