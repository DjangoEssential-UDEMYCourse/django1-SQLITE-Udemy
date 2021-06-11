from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

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


def produto(request, pk):
    # _produto_ = Produto.objects.get(id=pk)
    _produto_ = get_object_or_404(Produto, id=pk)
    context = {
        'produto': _produto_
    }
    return render(request, 'produto.html', context)


def error404(request, exception):
    _template = loader.get_template('status/404.html')
    return HttpResponse(content=_template.render(), content_type='text/html', charset='utf8', status=404)


def error500(request):
    _template = loader.get_template('status/500.html')
    return HttpResponse(content=_template.render(), content_type='text/html', charset='utf8', status=500)
