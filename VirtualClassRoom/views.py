from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# from .models import User

response = {
    "title" : "",
    "h1" : "",
}

def index(request):
    response["title"] = "VirtualClassRoom | welcome"
    response["h1"] = "view page index"
    
    return render(request, 'VirtualClassRoom/index.html', {'response' : response})

def login(request):
    response = "login page"
    return render(request, 'VirtualClassRoom/login.html', {'response' : response})

def mypage(request):      # removed user_id
    response = "test_user1"
    return render(request, 'VirtualClassRoom/mypage.html', {'response' : response})

def mypage2(request):      # removed user_id
    response = "test_user2"
    return render(request, 'VirtualClassRoom/mypage.html', {'response' : response})

def mypage3(request):      # removed user_id
    response = "test_user3"
    return render(request, 'VirtualClassRoom/mypage.html', {'response' : response})

def mypage4(request):      # removed user_id
    response = "form_user1"
    return render(request, 'VirtualClassRoom/mypage_form.html', {'response' : response})

def mypage5(request):      # removed user_id
    response = "form_user2"
    return render(request, 'VirtualClassRoom/mypage_form.html', {'response' : response})

def mypage6(request):      # removed user_id
    response = "form_user3"
    return render(request, 'VirtualClassRoom/mypage_form.html', {'response' : response})

 