from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadores(request):
    return render(request, "jogadores.html")

def sobre(request):
    return render(request, "sobre.html")