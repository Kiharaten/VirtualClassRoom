from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # ex: /students/
    path('<int:id>/join/', views.join, name='join'), # ex: /students/5/join/
    path('<int:id>/archive/', views.archive, name='archive'), # ex: /students/5/archive/
    path('<int:id>/mypage/', views.mypage, name='mypage'), # ex: /students/5/mypage/
]