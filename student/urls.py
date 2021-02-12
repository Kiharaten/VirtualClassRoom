from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # ex: /student/
    # path('login/',views.login, name='login'),
    # path('help/', views.help, name='help'),
    path('join/', views.join, name='join'),
    path('archive/', views.archive, name='archive'),
    path('mypage/', views.mypage, name='mypage'),
]