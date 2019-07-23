from django.shortcuts import render

# Create your views here.
def page(request):
    return render (request, 'index.html')

def redator(request):
    listaRedatores = ['Ana', 'Carolina', 'Eu']

    parametros = {
        'nome' = 'redator',
        'redator' = listaRedatores
    }

    return render(request, redatores.html, parametros)