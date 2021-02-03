from django.shortcuts import get_object_or_404, render

context = {
    'fixed': {
        'sitename': '遠隔授業システム',
        'title': '- 保護者ログイン -',
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
        'payment':'お支払い情報',
        'status':'学習状況',
        'notice':'お知らせ',
    },
}

# Create your views here.
def index(request):
    return render(request, 'parent/login.html', context)

def help(request):
    return render(request, 'parent/login.html', context)

def payment(request):
    context["fixed"]["title"] = context["nav"]["payment"]
    return render(request, 'parent/payment.html', context)

def status(request):
    context["fixed"]["title"] = context["nav"]["status"]
    return render(request, 'parent/status.html', context)

def notice(request):
    context["fixed"]["title"] = context["nav"]["notice"]
    return render(request, 'parent/notice.html', context)