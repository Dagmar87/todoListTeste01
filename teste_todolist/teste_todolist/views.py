from django.shortcuts import render
from .models import Tarefa, Categoria
from .forms import FormTarefa, FormCategoria

def index(request):
  return render(request, 'index.html')