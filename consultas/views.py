# O módulo views é responsavel por conter todas as funções que retornam informações ao usuário
# Para isso tambem será necessário receber as requisições


# O Django inclui o código das views por padrao a importação do django.shortcuts-render
# Este módulo é responsavel
from subprocess import IDLE_PRIORITY_CLASS
# HttpResponseRedirect é como o redirect do flask
from django.http import HttpResponse, HttpResponseRedirect
# reverse passa o nome da url ele gera a url
from django.urls import reverse
from django.shortcuts import render
# from django.template import loader

#importando as classses do arquivo models
from .models import Especialidades, Medico, Procedimentos
# Create your views here.
def especialidades(request):
    especialidades = Especialidades.objects.all()

    contexto = {'especialidades': especialidades}

    return render(request, 'especialidades.html', contexto)

def especialidade_detalhes(request, codigo_especialidade):
    # Para todos os modelos é possivel utilizar o metodo get que tem a função de fazer uma consulta no banco de dados e retorna somente um item
    # pk -> é um parametro possivel que faz referencia a primary key(chave primaria) definida no modelo
    especialidade = Especialidades.objects.get(codigo=codigo_especialidade)

    contexto = {'especialidade': especialidade}

    # return HttpResponse(f"Página detalhes dos medicos - ID do médico : {id_medico} - {medico.nome} ")
    return render(request, 'especialidade_detalhes.html', contexto)

def especialidade_cadastro(request):

    # TEM QUE SABER SE É POST
    if request.POST:

        nome = request.POST['nome']

        descricao = request.POST['descricao']

        especialidade = Especialidades(
            nome=nome,
            descricao=descricao
        )

        especialidade.save()
        return HttpResponseRedirect(reverse('especialidades'))

    return render(request, 'especialidade_cadastro.html')

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

def medico_cadastro(request):

    # pegando as especialidades
    especialidades = Especialidades.objects.all()

    contexto = {'especialidades': especialidades}

    # TEM QUE SABER SE É POST
    if request.POST:

        nome = request.POST['nome']

        email = request.POST['email']

        cpf = request.POST['cpf']

        crm = request.POST['crm']

        data_nascimento = request.POST['data_nascimento'] if request.POST['data_nascimento'] != "" else None

        cidade = request.POST['cidade']

        uf = request.POST['uf']

        especialidade_codigo = request.POST['especialidade']

        especialidade = Especialidades.objects.get(codigo=especialidade_codigo)

        medico = Medico(
            nome=nome,
            email=email,
            especialidade=especialidade,
            cpf=cpf,
            crm=crm,
            data_nascimento=data_nascimento,
            cidade=cidade,
            uf=uf
        )

        medico.save()
        # medicos = é o name da rota
        return HttpResponseRedirect(reverse('medicos'))

    return render(request, 'medico_cadastro.html', contexto)

def procedimentos(request):
    
    procedimentos = Procedimentos.objects.all()

    contexto = {'procedimentos': procedimentos}

    return render(request, 'procedimentos.html', contexto)

def procedimento_detalhes(request, codigo_procedimento):
   
    procedimento = Procedimentos.objects.get(codigo=codigo_procedimento)

    contexto = {'procedimento': procedimento}

    return render(request, 'procedimento_detalhes.html', contexto)

def procedimento_cadastro(request):

    # TEM QUE SABER SE É POST
    if request.POST:

        nome = request.POST['nome']

        descricao = request.POST['descricao']

        procedimento = Procedimentos(
            nome=nome,
            descricao=descricao
        )

        procedimento.save()
        return HttpResponseRedirect(reverse('procedimentos'))

    return render(request, 'procedimento_cadastro.html')

