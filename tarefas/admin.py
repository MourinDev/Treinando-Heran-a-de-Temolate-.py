from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'concluida', 'criada_em')
    list_filter = ('concluida', 'criada_em')
    search_fields = ('titulo', 'descricao')
    ordering = ('-criada_em',)

admin.site.register(Tarefa, TarefaAdmin)