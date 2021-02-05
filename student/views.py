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
    'join':{
        'list':{
            '00000123':{
                'subject':'数',
                'class':'A',
                'title':'おはじきを取り出す確率',
                'description':'確率の計算について、導入と理解。簡単な例題を講師と一緒に解いてみましょう。',
            },
            '00000122':{
                'subject':'現',
                'class':'文',
                'title':'素早く読み取る読解力',
                'description':'参考書「入試現文へのアクセス」の解説、要点の押さえ方を講師と一緒に実践形式で学びましょう。',
            },
            '00000121':{
                'subject':'地',
                'class':'理',
                'title':'講義タイトル',
                'description':'説明文',
            },
            '00000120':{
                'subject':'化',
                'class':'学',
                'title':'講義タイトル',
                'description':'説明文',
            },
        },
    },
    'archive':{
        'list': {
            '00000121': {
                'subject': '地',
                'class': '理',
                'title': '講義タイトル',
                'description': '説明文',
            },
            '00000120': {
                'subject': '化',
                'class': '学',
                'title': '講義タイトル',
                'description': '説明文',
            },
            '00000119': {
                'subject': '英',
                'class': '表',
                'title': '講義タイトル',
                'description': '説明文',
            },
            '00000118': {
                'subject': '歴',
                'class': '史',
                'title': '講義タイトル',
                'description': '説明文',
            },
        },
    },
    'mypage':{
        'logout':'ログアウト',

    },
    'nav':{
        'join':'講義に参加',
        'archive':'ビデオ視聴',
        'mypage':'マイページ',
    },
}

# Create your views here.
def index(request):
    return render(request, 'student/login.html', context)

def help(request):
    return render(request, 'student/help.html', context)

def join(request):
    context["fixed"]["title"] = context["nav"]["join"]
    return render(request, 'student/join.html', context)

def archive(request):
    context["fixed"]["title"] = context["nav"]["archive"]
    return render(request, 'student/archive.html', context)

def mypage(request):
    context["fixed"]["title"] = context["nav"]["mypage"]
    return render(request, 'student/mypage.html', context)
