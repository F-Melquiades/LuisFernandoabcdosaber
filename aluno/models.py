from django.db import models
from django.urls import reverse

# Create your models here.
class Aluno(models.Model):
    """ Modelo representando um Aluno """
    matricula = models.AutoField(primary_key=True, null=False, help_text='Matrícula do Aluno')
    nome = models.CharField(max_length=70, null=False, help_text='Informe o nome do Aluno')
    dataMatricula = models.DateField(max_length=70, null=False, help_text='Informe a Data da Matrícula do Aluno')
    dataSaida = models.DateField(max_length=70, null=True, blank=True, help_text='Informe a Data de Saída do Aluno')
    
    def __str__(self):
        return f'{self.matricula} {self.nome} {self.dataMatricula} {self.dataSaida}'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})