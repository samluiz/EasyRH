from django.db import models

class Candidato(models.Model):
  nome = models.TextField(max_length=100, blank=False)
  dataDeNascimento = models.DateField(auto_now=False, auto_now_add=False, blank=True)
  cpf = models.TextField(max_length=11, blank=True)
  curriculo = models.FileField(upload_to='', storage=None, max_length=100, blank=True)

  def __str__(self):
    return self.nome