def preset():
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

    return context