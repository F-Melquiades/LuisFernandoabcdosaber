from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse('<h3>Esta é a página de Tipo de Atividade<h3>')
def fim(request):
    return HttpResponse('<h3>This is the end<h3>')
def cadastrar(request):
    return render (request, 'tipoatividade/cadastrotiposatividade.html')
def listar (request):
    return render(request, 'tipoatividade/listartiposatividade.html')