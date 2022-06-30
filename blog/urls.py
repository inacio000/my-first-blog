"""
Importando do Django a função url
e todas as nossas views do aplicativo blog.

views.post_list é o lugar correto aonde ir se alguém entra em seu site pelo endereço 'http://127.0.0.1:8000 /'

name='post_list', é o nome da URL que será usado para identificar a view
"""
from django.urls import path
from . import views

# A parte post/<int:pk>/ especifica um padrão de URL
# post/ significa apenas que a URL deve começar com a palavra post seguida por /
# <int:pk> – Ela nos diz que o Django espera um objeto do tipo inteiro e que vai transferi-lo para a view como uma variável chamada pk
# / – por fim, precisamos adicionar uma / ao final da nossa URL

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
