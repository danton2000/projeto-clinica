# O arquivo urls.py é responsavel por tratar o direcionamento das rotas,
#  conforme a requisões do usuário
from django.urls import path
# importa a view do app
from . import views
# rotas do app

# variável obrigatória
# A variável urlpatterns é uma lista, e a ordem dos itens importam
urlpatterns = [
    # A função path é responsavel por estruturar a rota da aplicação

    # name = serve para nomear as rotas, podemos chamar as rotas pelo nome pela tag <a> do html

    # estrutura das rotas dessa aplicação:
    # Aplicação/Model/função(listar, cadastrar, detalhes)

    path('', views.index, name="index"),

    # fixa rotas
    path('especialidades/listar/', views.especialidades, name="especialidades"),
    path('especialidades/cadastrar/', views.especialidade_cadastro, name="especialidade_cadastrar"),
    path('medicos/listar/', views.medicos, name="medicos"),
    path('medicos/cadastrar/', views.medico_cadastro, name="medico_cadastrar"),
    path('procedimentos/listar/', views.procedimentos, name="procedimentos"),
    path('procedimentos/cadastrar/', views.procedimento_cadastro, name="procedimento_cadastrar"),
    path('consultas/listar/', views.consultas, name="consultas"),
    path('consultas/cadastrar/', views.consulta_cadastro, name="consulta_cadastrar"),

    # dinamicas rotas
    path('especialidades/detalhes/<codigo_especialidade>', views.especialidade_detalhes, name="especialidade_detalhes"),
    path('medicos/detalhes/<id_medico>', views.medico_detalhes, name="medico_detalhes"),
    path('procedimentos/detalhes/<codigo_procedimento>', views.procedimento_detalhes, name="procedimento_detalhes"),
    path('consultas/detalhes/<codigo_consulta>', views.consulta_detalhes, name="consulta_detalhes")
]
