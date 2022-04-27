from django.db import models

# Create your models here.

class Curso(models.Model):                          # Curso es un modelo que hereda de models de django
    nombre= models.CharField(max_length=50)         # CharField tipo de strings para modelos
    comision=models.IntegerField()

class Estudiantes(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField(max_length=50)

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    profesion = models.CharField(max_length=50)

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_de_entrega= models.DateField()
    entregado=models.BooleanField()