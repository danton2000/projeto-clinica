from django.db import models

# Create your models here.


# O modelo(models) trata-se de uma classe que extends models.Model
# Este models já possui diversos recursos para o uso de banco de dados e interfaces.
# Como atribui id, que cria um identificador unico para o registro e o objects, que
# trata modulo manage que nos possibilita criar comandos de consulta no banco de de dados

class Medico(models.Model):

    pass

"""
    Nome
    CPF
    CRM
    Idade
    Cidade
    E-mail
"""