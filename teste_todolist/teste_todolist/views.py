from django.shortcuts import render
from .models import Tarefa, Categoria
from .forms import FormTarefa, FormCategoria

def index(request):
  return render(request, 'index.html')

def categorias(request):
  categorias = Categoria.objects.all()
  return render(request, 'categorias.html', {'categorias': categorias})