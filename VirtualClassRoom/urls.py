from django.urls import path

from . import views

app_name = 'VirtualClassRoom'

urlpatterns = [
    path('',views.index, name='index'),                     # domain.com/VirtualClassRoom/
    path('login/', views.login, name='login'),              # domain.com/VirtualClassRoom/login/
    path('test_user1', views.mypage, name='mypage'),        # domain.com/VirtialClassRoom/test_user1
    # path('test_user2', views.mypage2, name='mypage'),        # domain.com/VirtialClassRoom/test_user2
    # path('test_user3', views.mypage3, name='mypage'),        # domain.com/VirtialClassRoom/test_user3
    # path('form_user1', views.mypage4, name='mypage'),        # domain.com/VirtialClassRoom/form_user1
    # path('form_user2', views.mypage5, name='mypage'),        # domain.com/VirtialClassRoom/form_user2
    # path('form_user3', views.mypage6, name='mypage'),        # domain.com/VirtialClassRoom/form_user3
]