from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Area(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    descricao = RichTextField(blank=True, null=True)
    cor = models.CharField(max_length=7, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class SubArea(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = RichTextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    areas = models.ManyToManyField(Area)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Plataforma(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    descricao = RichTextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    areas = models.ManyToManyField(Area)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Pessoa(models.Model):
    objects = None
    nome = models.CharField(max_length=50, unique=True)
    descricao = RichTextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    areas = models.ManyToManyField(Area)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class InicioAtividade(models.Model):
    inicio = models.DateTimeField(blank=False, null=False)


class Atividade(models.Model):
    data = models.DateField()
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    subarea = models.ForeignKey(SubArea, on_delete=models.PROTECT)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    detalhamento = RichTextField(blank=True, null=True)
    tempo = models.IntegerField()
    inicio = models.DateTimeField(blank=True, null=True)
    fim = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['-data']
