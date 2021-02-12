from django.shortcuts import get_object_or_404, render

context = {
    'fixed': {
        'sitename': '遠隔授業システム',
        'title': '- サイト情報 -',
    },
}
# Create your views here.

def index(request):
    return render(request, 'information/top.html', context)

def help(request):
    return render(request, 'information/help.html', context)