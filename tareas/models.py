from django.db import models

# Create your models here.
class Tareas(models.Model):
    Titulo = models.CharField()
    descripcion = models.CharField()
    fecha = models.DateField()
    
    
def __str__(self):
    return self.Titulo 
    