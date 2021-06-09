from django.shortcuts import render


def index(request):
    print(dir(request.user))
    print(f'User: { request.user }')
    if str(request.user) == "AnonymousUser":
        _usuario_logado_ = 'Usuário não Logado'
    else:
        _usuario_logado_ = 'Usuário Logado'
    context = {
        'curso': 'Programação WEB com Django Framework',
        'usuario_logado': _usuario_logado_
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
