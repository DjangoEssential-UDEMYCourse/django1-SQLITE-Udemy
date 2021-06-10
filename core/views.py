from django.shortcuts import render
from .models import Produto


def index(request):
    print(dir(request.user))
    print(f'User: { request.user }')
    
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação WEB com Django Framework',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
