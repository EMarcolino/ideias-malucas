from django.shortcuts import render

# Create your views here.

def index(request):
    contexto = {
    }
    return render(request, 'index.html', contexto)

def sobre(request):
    contexto = {

    }
    return render(request, 'sobre.html', contexto)