from django.shortcuts import render

def tela_inicial(request):
    return render(request, 'core/tela_inicial.html')
