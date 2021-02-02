from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # ex: /student/
    path('/join/', views.join, name='join'), # ex: /student/5/join/
    path('<int:student_id>/archive/', views.archive, name='archive'), # ex: /student/5/archive/
    path('<int:student_id>/mypage/', views.mypage, name='mypage'), # ex: /student/5/mypage/
]