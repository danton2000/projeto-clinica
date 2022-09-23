# O módulo views é responsavel por conter todas as funções que retornam informações ao usuário
# Para isso tambem será necessário receber as requisições


# O Django inclui o código das views por padrao a importação do django.shortcuts-render
# Este módulo é responsavel
from subprocess import IDLE_PRIORITY_CLASS
from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader

from .models import Medico
# Create your views here.
# Por definição as funções de visualização precisam obrigatório ter
# um paramentro de request
def medicos(request):
    #Utilizar o modelo (para este caso Medico) para buscar do banco de dados todos os médicos
    #Pegando todos os medicos de Models
    medicos = Medico.objects.all()

    # Variavel do tipo dicionário que setá responsável por armazenar o contexto que será enviado para o template
    contexto = {'medicos': medicos}

    # Motor de template
    # Preparando o motor do template
    # template = loader.get_template("medicos.html")

    # Já o retorno será uma responsta HTTP para isso será necessário utilizar a função 'HttpResponse'
    # return HttpResponse(template.render(contexto, request))

    # PREPARANDO O TEMPLATE E RETORNA PARA O USUÁRIO COM O CONTEXTO
    # Quando os módulos do shortcut são utilizados é reduzido o volumo de código(ATALHO)
    # No caso render, é necessário colocar como primeiro parâmetro o request(como paramentro da function view), em segundo o template e por ultimo o contexto(conjunto de dados)
    return render(request, 'medicos.html', contexto)

# Função desenvolvimento para formação os detalhes do médico, para isso foi necessário que forem declarado, o parametro id_medico para receber a informacao vinda da URL
def medico_detalhes(request, id_medico):
    # Para todos os modelos é possivel utilizar o metodo get que tem a função de fazer uma consulta no banco de dados e retorna somente um item
    # pk -> é um parametro possivel que faz referencia a primary key(chave primaria) definida no modelo
    medico = Medico.objects.get(pk=id_medico)

    contexto = {'medico': medico}

    # return HttpResponse(f"Página detalhes dos medicos - ID do médico : {id_medico} - {medico.nome} ")
    return render(request, 'medico_detalhes.html', contexto)