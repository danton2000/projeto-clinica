# O módulo views é responsavel por conter todas as funções que retornam informações ao usuário
# Para isso tambem será necessário receber as requisições

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Por definição as funções de visualização precisam obrigatório ter
# um paramentro de request
def medicos(request):
    # Já o retorno será uma responsta HTTP para isso será necessário utilizar a função 'HttpResponse'
    return HttpResponse("Está é a página de médicos")