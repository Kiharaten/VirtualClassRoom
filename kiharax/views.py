# from django.shortcuts import render

# # Create your views here.

# def index(request):
#     return render(request, 'index.html')

#from django.shortcuts import render

# Create your views here.

# ex:
    # index       -> /kiharax/
    # name        -> /kiharax/name/
    # gender      -> /kiharax/gender/
    # age         -> /kiharax/age/
    # height      -> /kiharax/height/
    # weight      -> /kiharax/weight/
    # description -> /kiharax/description/

from django.http import HttpResponse, Http404
# from django.shortcuts import get_object_or_404, render
profile = {
    "name" : "Hi, my name is Sora Kihara.",
    "gender" : "Yeah, my gender is men.",
    "age" : "Ok, my age is 20 years old.",
    "height" : "No problem, my height is about 170cm.",
    "weight" : "sure, my weight is about 55kg.",
}


def index(request):
    return HttpResponse("Hello, world. You're at the kiharax index.")

def name(request):
    return HttpResponse(profile["name"])

def gender(request):
    return HttpResponse(profile["gender"])

def age(request):
    return HttpResponse(profile["age"])

def height(request):
    return HttpResponse(profile["height"])

def weight(request):
    return HttpResponse(profile["weight"])

def description(request):
    description = ""
    for value in profile.values():
        description = description + value + " "
    return HttpResponse(description)