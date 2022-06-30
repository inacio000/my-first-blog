"""
Importando do Django a função url
e todas as nossas views do aplicativo blog.

views.post_list é o lugar correto aonde ir se alguém entra em seu site pelo endereço 'http://127.0.0.1:8000 /'

name='post_list', é o nome da URL que será usado para identificar a view
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list')
]
