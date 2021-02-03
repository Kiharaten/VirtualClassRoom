def var_config(self):
    """
    規定値指定
    """
    context = {
        'student': {
            'fixed': {
                'sitename': '遠隔授業システム',
                'title': '',
            },
            'nav':{
                'join':'講義に参加',
                'archive':'ビデオ視聴',
                'mypage':'マイページ',
            }
        },
        'parent': {
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
    }

    return context