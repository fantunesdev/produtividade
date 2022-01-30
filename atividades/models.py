from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Area(models.Model):
    nome = models.CharField(max_length=20, unique=True, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    cor = models.CharField(max_length=7, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome


class SubArea(models.Model):
    nome = models.CharField(max_length=50, unique=True, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, default=666)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class InicioAtividade(models.Model):
    inicio = models.DateTimeField(blank=False, null=False)


class Atividade(models.Model):
    data = models.DateField(default=timezone.localtime(timezone.now()))
    area = models.ForeignKey(Area, on_delete=models.SET_DEFAULT, default=666)
    sub_area = models.CharField(max_length=50, blank=True, null=True)
    plataforma = models.CharField(max_length=30, blank=True, null=True)
    pessoa = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    detalhamento = RichTextField(blank=True, null=True)
    tempo = models.IntegerField(blank=False, null=False)
    inicio = models.DateTimeField(blank=True, null=True)
    fim = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.descricao


class Plataforma(models.Model):
    nome = models.CharField(max_length=30, unique=True, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Pessoa(models.Model):
    nome = models.CharField(max_length=50, unique=True, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
