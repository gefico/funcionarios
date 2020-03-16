from django.shortcuts import render
from .models import Funcionario
from django.views.decorators.csrf import csrf_protect

def listagem(request):
    titulo = 'Listagem de Funcionarios'
    funcionarios = Funcionario.objects.all()
    return render(request, 'listagem.html',{'titulo': titulo , 'funcionarios':funcionarios})

def selecao(request, id):
    titulo = 'Listagem de Funcionarios'
    funcionario = Funcionario.objects.get(id=id)
    return render(request, 'listagem.html',{'titulo': titulo , 'funcionarios':[funcionario]})

@csrf_protect
def consulta(request):
    consulta =request.POST.get('consulta')
    campo = request.POST.get('campo')
    
    if campo == 'nome':
        funcionarios = Funcionario.objects.filter(nome_contains=consulta)
    elif campo == 'idade':
        funcionarios = Funcionario.objects.filter(idade_contains=consulta)
    elif campo == 'sexo':
        funcionarios = Funcionario.objects.filter(sexo_contains=consulta)
    elif campo == 'salario':
        funcionarios = Funcionario.objects.filter(salario_contains=consulta)

    titulo = 'Listagem de Pessoas'

    return render(request, 'listagem.html', {'titulo':titulo, 'funcionarios': funcionarios})


