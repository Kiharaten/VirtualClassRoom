# from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
    response = "view index data"
    # return render(request, 'VirtualClassRoom/index.html', {'response' : response})
    return HttpResponse(response)

