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
    path('', views.medicos),
    #fixa rotas
    path('medicos/listar/', views.medicos, name="medicos"),
    path('medicos/cadastrar/', views.medico_cadastro , name="medico_cadastrar"),
    path('procedimentos/listar/', views.procedimentos, name="procedimentos"),
    #dinamicas rotas
    path('medicos/detalhes/<id_medico>', views.medico_detalhes, name="medico_detalhes"),
    path('procedimentos/detalhes/<id_procedimento>', views.procedimento_detalhes, name="procedimento_detalhes")
]