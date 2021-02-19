from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # ex: /information/
    path('help/', views.help, name='help'),
]