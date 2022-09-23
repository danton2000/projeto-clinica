from django.contrib import admin

# Register your models here.
# Importa o modulo(MODELS) criado dentro do arquivo models.py
# Sendo assim é necessário a uitlização do .models visto que models é o nome do módulo e o ".", é a estrutura do pacote (package) 
from .models import Especialidades, Procedimentos, Medico

# O registro é feito atráves do modulo contrib, previamente importado pelo Django
# Para acontecer o registro é necessário dentro do atributo "site" executar o método "register()"
# passando como paramentro o modelo(Models), para este caso Medico
admin.site.register(Medico)
admin.site.register(Procedimentos)
admin.site.register(Especialidades)