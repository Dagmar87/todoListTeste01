from django.db import models

class Categoria(models.Model):
  nome = models.CharField(max_length=50)
  descricao = models.TextField()
  
  def __str__(self):
			return self.nome
 
	
class Status(models.Model):
  nome = models.CharField(max_length=50)
  descricao = models.TextField()
  
  def __str__(self):
			return self.nome
 
	
class Tarefa(models.Model):
  categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
  status_id = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
  titulo = models.CharField(max_length=50)
  descricao = models.TextField()
  data_de_vencimento = models.DateTimeField()
  
  def __str__(self):
			return self.titulo
	