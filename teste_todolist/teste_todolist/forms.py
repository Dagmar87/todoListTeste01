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
			'categoria': forms.Select(attrs={'class': 'form-control'}),
      'status': forms.Select(attrs={'class': 'form-control'}),
      'descricao': forms.TextInput(attrs={'class': 'form-control'}),
      'data_de_vencimento': DateTimePickerInput(attrs={'class': 'form-control'}),
		}