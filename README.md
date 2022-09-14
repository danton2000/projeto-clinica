# projeto-clinica
Projeto feito com Django

A proposta deste projeto é construir uma aplicação web irá atender uma clinica

O objetivo é desenvolver as seguintes telas:

- Médicos

- Especialidades

- Procedimentos

- Consultas

## Preparar o ambiante

Instalando o venv
"""
    python -m venv venv
"""

Ativando o venv
"""
    .\venv\script\activate
"""

Instalação do Django
"""
    pip install django
"""

Colocando as versões do pacote em um arquivo .txt
"""
    pip freeze > requirents.txt
"""

### Estruturação do Projeto

1. Criar o projeto
NOTE: Projeto é o local que o motor do Django é executado, com isso as configurações são feitas dentro dele,
utilizando o arquivo settings.py

Criando projeto no django
"""
   django-admin startproject nome-do-projeto .
"""

- django-admin: comando de terminal responsável pela administração do Django
    - startproject: Parametro do comando django-admin responsável por estruturar um projeto em django
        È obrigatório o nome do projeto (neste caso "clinica")
        Como proximo parametro é o diretório que será executado o projeto, que a sugestão é informar o caminho relativo do diretório local "."

#### Iniciar o serviço web
"""
    python -m manage runserver
"""

- manage: Módulo do Django responsável por executar ações dentro do projeto
    - runserver: Parametro que determina a execução do módulo web disponível dentro do Django para desenvolvimento

O site estará disponivel no endereço "http://127.0.0.1:8000/"

2. Criar um APP

NOTE: O APP (aplicação) será o local no Django que setá implementado toda a lógica. Lembrando que um projeto pode ter vários APPs.
