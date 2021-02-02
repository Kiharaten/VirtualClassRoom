from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # ex: /parent/
    path('payment/', views.payment, name='payment'), # ex: /parent/payment/
    path('status/', views.status, name='status'), # ex: /parent/status/
    path('notice/', views.notice, name='notice'), # ex: /parent/notice/
]