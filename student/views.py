from django.shortcuts import get_object_or_404, render

context = {
    'fixed': {
        'sitename': '遠隔授業システム',
        'title': '',
    },
    'nav':{
        'join':'講義に参加',
        'archive':'ビデオ視聴',
        'mypage':'マイページ',
    }
}

# Create your views here.
def index(request):
    context["fixed"]["title"] = "login"
    return render(request, 'student/login.html', context)
    # return HttpResponse("you can login from here.")

def join(request):
    context["fixed"]["title"] = context["nav"]["join"]
    return render(request, 'student/join.html', context)
    # return HttpResponse("you can join classroom from here.")

def archive(request):
    context["fixed"]["title"] = context["nav"]["archive"]
    return render(request, 'student/archive.html', context)
    # return HttpResponse("you can see archive from here.")

def mypage(request):
    context["fixed"]["title"] = context["nav"]["mypage"]
    return render(request, 'student/mypage.html', context)
    # return HttpResponse("you can check mypage here.")
