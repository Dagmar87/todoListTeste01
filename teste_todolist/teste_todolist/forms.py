from django.forms import ModelForm
from django import forms
from .models import Tarefa, Categoria

class DateTimePickerInput(forms.DateTimeInput):
  input_type = 'datetime-local'
  
class FormTarefa(ModelForm):
  class Meta:
    model = Tarefa
    fields = '__all__'
    widgets = {
			'titulo': forms.TextInput(attrs={'class': 'form-control'}),
			'categoria_id': forms.Select(attrs={'class': 'form-control'}),
      'status_id': forms.Select(attrs={'class': 'form-control'}),
      'descricao': forms.TextInput(attrs={'class': 'form-control'}),
      'data_de_vencimento': DateTimePickerInput(attrs={'class': 'form-control'}),
		}
    
class FormCategoria(ModelForm):
  class Meta:
    model = Categoria
    fields = '__all__'
    widgets = {
			'nome': forms.TextInput(attrs={'class': 'form-control'}),
		  'descricao': forms.TextInput(attrs={'class': 'form-control'}),
		}