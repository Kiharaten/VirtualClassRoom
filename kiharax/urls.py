from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('name', views.name, name='name'),
    path('gender', views.gender, name='gender'),
    path('age', views.age, name='age'),
    path('height', views.height, name='height'),
    path('weight', views.weight, name='weight'),
    path('description', views.description, name='description'),

    # ex:
    # index       -> /kiharax/
    # name        -> /kiharax/name/
    # gender      -> /kiharax/gender/
    # age         -> /kiharax/age/
    # height      -> /kiharax/height/
    # weight      -> /kiharax/weight/
    # description -> /kiharax/description/
]