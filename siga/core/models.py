from django.db import models
from django.contrib.auth.models import Group, User

class AuditEntity(models.Model):
    
    # Salvando automaticamente as datas de criação e atualização dos dados
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AbstractEntity(AuditEntity):
    
    nome = models.CharField(max_length=200) 

    def __str__(self):
        return self.nome 
    
    class Meta:
        abstract = True

class NucleoIncubador (Group):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Nucleo_Incubadores"

class Servidor(AuditEntity):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    nucleo_incubador = models.ForeignKey(NucleoIncubador,on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        fullname = self.usuario.first_name + " " + self.usuario.last_name + " ({})".format(self.usuario.username)
        return fullname
    
    class Meta:
        verbose_name_plural = "Servidores"
