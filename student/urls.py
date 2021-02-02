from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # ex: /student/
    path('join/', views.join, name='join'), # ex: /student/join/
    path('archive/', views.archive, name='archive'), # ex: /student/archive/
    path('mypage/', views.mypage, name='mypage'), # ex: /student/mypage/
]