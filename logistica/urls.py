from django.conf.urls import url
from django.urls import path, include

from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('buscar_para_seguir', views.buscar_para_seguir, name='buscar_para_seguir'),
]