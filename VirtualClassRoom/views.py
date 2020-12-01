from django.shortcuts import render, get_object_or_404

def index(request):
    response = "view index data"
    return render(request, 'index.index.html', {'response' : response})

