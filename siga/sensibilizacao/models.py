from django.db import models
from core.models import Servidor

class Palestra(models.Model):
    titulo = models.CharField(max_length=200) 
    descricao = models.TextField()
    aprendizado = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    servidor = models.ForeignKey(Servidor,on_delete=models.CASCADE, blank=True)