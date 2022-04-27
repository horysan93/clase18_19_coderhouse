from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.
def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto=f"---->Curso:  {curso.nombre} comisión: {curso.comision}"
    return HttpResponse(texto)
