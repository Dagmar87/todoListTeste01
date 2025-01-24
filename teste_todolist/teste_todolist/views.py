import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_list_or_404
from .models import Tarefa, Categoria
from .forms import FormTarefa, FormCategoria

def index(request):
  return render(request, 'index.html')

def Categoria_View(request):
  return render(request, 'categorias_list.html', {
		'categoria': Categoria.objects.all,
  	'titulo': "Categoria"
	})
  
def TodoList_View(request):
  return render(request, 'tarefa_list.html', {
    'tarefas_a_fazer': Tarefa.objects.filter(status_id=1).order_by('data_de_vencimento'),
    'tarefas_em_andamento': Tarefa.objects.filter(status_id=2).order_by('data_de_vencimento'),
    'tarefas_concluidas': Tarefa.objects.filter(status_id=3).order_by('data_de_vencimento'),
    'tarefas_abandonadas': Tarefa.objects.order_by('data_de_vencimento').filter(status_id=4).order_by('data_de_vencimento'),
		'contagem_de_tarefas': Tarefa.objects.filter(status_id=1).count(),
    'contagem_continua': Tarefa.objects.filter(status_id=2).count(),
    'contagem_concluida': Tarefa.objects.filter(status_id=3).count(),
    'contagem_abandonada': Tarefa.objects.filter(status_id=4).count(),
    'titulo': "Listadetarefas"
	})
  
def tarefa_add(request):
    if request.method == "POST":
        form = FormTarefa(request.POST)
        if form.is_valid():
            tarefa = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "TarefaListChanged": None,
                        "showMessage": f"{tarefa.titulo} adicionado."
                    })
                })
    else:
        form = FormTarefa()
    return render(request, 'tarefa_form.html', {
        'form': form,
    })
    
def categoria_add(request):
    if request.method == "POST":
        form = FormCategoria(request.POST)
        if form.is_valid():
            categoria = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "TarefaListChanged": None,
                        "showMessage": f"{categoria.nome} adicionado."
                    })
                })
    else:
        form = FormCategoria()
    return render(request, 'categoria_form.html', {
        'form': form,
    }) 
    
def tarefa_edit(request, id):
    tarefa = get_list_or_404(Tarefa, id=id)
    if request.method == "POST":
        form = FormTarefa(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "categoriaListChanged": None,
                        "showMessage": f"{tarefa.titulo} atualizado."
                    })
                }
            )
    else:
        form = FormTarefa(instance=tarefa)
    return render(request, 'tarefa_form.html', {
        'form': form,
        'tarefa': tarefa,
    }) 
    
def categoria_edit(request, id):
    categoria = get_list_or_404(Categoria, id=id)
    if request.method == "POST":
        form = FormCategoria(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "categoryListChanged": None,
                        "showMessage": f"{categoria.nome} atualizado."
                    })
                }
            )
    else:
        form = FormCategoria(instance=categoria)
    return render(request, 'categoria_form.html', {
        'form': form,
        'categoria': categoria,
    })