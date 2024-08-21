from django.urls import path
from turma import views

urlpatterns = [
    path('', views.cadastrar, name='cadastrar_turma'),
    path('listar/', views.listar, name='listar_turma')
]