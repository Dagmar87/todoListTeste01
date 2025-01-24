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

def todolist(request):
  categorias = Categoria.objects.all()
  statuses = Status.objects.all()
  if request.method == "POST":
    categoria_filter = request.POST.get("categoria_filter")
    status_filter = request.POST.get("status_filter")
    if categoria_filter and status_filter:
      tarefas = Tarefa.objects.filter(categoria=categoria_filter, status=status_filter).order_by('data_de_vencimento')
    elif categoria_filter:
      tarefas = Tarefa.objects.filter(categoria=categoria_filter).order_by('data_de_vencimento')
    elif status_filter:
      tarefas = Tarefa.objects.filter(status=status_filter).order_by('data_de_vencimento')
    else:
      tarefas = Tarefa.objects.all().order_by('data_de_vencimento')
  else:
    tarefas = Tarefa.objects.all().order_by('data_de_vencimento')
    
  return render(request, 'todolist.html',{
		'tarefas': tarefas, 'categorias': categorias, 'statuses': statuses
	})