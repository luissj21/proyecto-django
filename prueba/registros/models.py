from django.db import models
# Create your models here.

class Alumnos(models.Model): #Define la estructura de la tabla
    matricula = models.CharField(max_length=12, verbose_name="Mat") #Texto Corto
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
    
    