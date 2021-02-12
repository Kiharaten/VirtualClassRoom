from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # ex: /parent/
    # path('login/',views.login, name='login'),
    # path('help/', views.help, name='help'),
    path('payment/', views.payment, name='payment'),
    path('status/', views.status, name='status'),
    path('notice/', views.notice, name='notice'),
]