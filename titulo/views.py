from django.shortcuts import render
from titulo.models import Titulo
from titulo.forms import TituloForm

def cadastrar(request):
    return render(request, 'titulo/cadastroTitulos.html')

def listar(request):
    
    registros = Titulo.objects.all()
    
    contexto = {'tipos_titulo_lista': registros}
    
    return render(request, 'titulo/listarTitulos.html', contexto)

def cadastro(request):
    
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(
            descricao = dados_titulo['descricao']
        )
        titulo.save()
        
    return render(request, 'titulo/cadastroTitulos.html')