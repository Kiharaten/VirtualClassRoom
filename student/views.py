from django.shortcuts import get_object_or_404, render

context = {
    'fixed': {
        'sitename': '遠隔授業システム',
        'title': '- 生徒ログイン -',
    },
    'login':{
        'username':'ユーザー名を入力',
        'password':'パスワードを入力',
        'login':'ログイン',
        'student':'生徒ログイン',
        'parent':'保護者ログイン',
        'help':'ログインできない場合',
    },
    'nav':{
        'join':'講義に参加',
        'archive':'ビデオ視聴',
        'mypage':'マイページ',
    },
}

# Create your views here.
# get
def index(request):
    return render(request, 'student/login.html', context)

def help(request):
    return render(request, 'parent/login.html', context)

def join(request):
    context["fixed"]["title"] = context["nav"]["join"]
    return render(request, 'student/join.html', context)

def archive(request):
    context["fixed"]["title"] = context["nav"]["archive"]
    return render(request, 'student/archive.html', context)

def mypage(request):
    context["fixed"]["title"] = context["nav"]["mypage"]
    return render(request, 'student/mypage.html', context)


# post
def login(request, username, password):
    # get_object_or_404()
    return join(request)
