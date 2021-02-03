from django.shortcuts import get_object_or_404, render

context = {
    'fixed': {
        'sitename': '遠隔授業システム',
        'title': '',
    },
    'nav':{
        'payment':'お支払い情報',
        'status':'学習状況',
        'notice':'お知らせ',
    }
}

# Create your views here.
def index(request):
    context["fixed"]["title"] = "login"
    return render(request, 'parent/login.html', context)
    # return HttpResponse("you can login from here.")

def payment(request):
    context["fixed"]["title"] = context["nav"]["payment"]
    return render(request, 'parent/payment.html', context)
    # return HttpResponse("you can join classroom from here.")

def status(request):
    context["fixed"]["title"] = context["nav"]["status"]
    return render(request, 'parent/status.html', context)
    # return HttpResponse("you can see archive from here.")

def notice(request):
    context["fixed"]["title"] = context["nav"]["notice"]
    return render(request, 'parent/notice.html', context)
    # return HttpResponse("you can check mypage here.")