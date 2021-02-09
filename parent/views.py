from django.shortcuts import get_object_or_404, render
# import preset
context = {
    'fixed': {
        'sitename': '遠隔授業システム',
        'title': '- 保護者ログイン -',
    },
    'login':{
        'username':'ユーザー名を入力',
        'password':'パスワードを入力',
        'login':'ログイン',
        'path':'/student/',
        'parent':'保護者ログイン',
        'student':'生徒ログイン',
        'help':'ログインできない場合',
    },
    'payment':{
        'list':{
            '00000123':{
                # 'image':'static/hoge.png',
                'title':'遠隔授業システムProプラン',
                'price':'￥3000.00円',
                'length':'1ヶ月',
            },
            # '00000122':{
            #     'image':'static/hoge.png',
            #     'title':'遠隔授業システムProプラン',
            #     'price':'3000.00',
            #     'length':'1ヶ月',
            # },
            # '00000121':{
            #     'image':'static/hoge.png',
            #     'title':'遠隔授業システムProプラン',
            #     'price':'3000.00',
            #     'length':'1ヶ月',
            # },
            # '00000120':{
            #     'image':'static/hoge.png',
            #     'title':'遠隔授業システムProプラン',
            #     'price':'3000.00',
            #     'length':'1ヶ月',
            # },
        },
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

# def login(request):
#     return render(request, 'student/login,html', context)

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