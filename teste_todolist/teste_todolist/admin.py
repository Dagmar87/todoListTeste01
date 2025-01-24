from django.contrib import admin

from .models import Categoria, Status, Tarefa

class TarefaAdmin(admin.ModelAdmin):
  list_display = ['categoria_id', 'status_id', 'titulo', 'descricao', 'data_de_vencimento']
  search_fields = ['titulo']
  list_filter = ('categoria_id', 'status_id')
  list_per_page = 10
  
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Categoria)
admin.site.register(Status)