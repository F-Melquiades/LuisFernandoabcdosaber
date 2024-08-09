from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h3>Esta é a página de index<h3>')

def abc123(request):
    return HttpResponse('<h3>pagina abc<h3>')

def escola(request):
    return render(request, 'escola.html')

