from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.
def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto=f"---->Curso:  {curso.nombre} comisión: {curso.comision}"
    return HttpResponse(texto)

# Creamos paginas de cada una de los modelos
#def inicio(request):
#    return HttpResponse("Esta es la pagina de inicio")

#vamos acambiar inicio
def inicio(request):
    return render(request,"AppCoder/inicio.html")

# Creamos paginas para cada clase que utilizamos: profesores, estudiants, cursos, entregables 
def profesores(request):
    return HttpResponse("Esta es la pagina de profesores")

def estudiantes(request):
    return HttpResponse("Esta es la pagina de estudiantes")

def cursos(request):
    return HttpResponse("Esta es la pagina de cursos")

def entregables(request):
    return HttpResponse("Esta es la pagina de entregables")

