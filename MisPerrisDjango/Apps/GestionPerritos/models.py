from django.db import models

# Create your models here.

class Perritos(models.Model):
	codigo = models.PositiveIntegerField()
	nombre = models.CharField(max_length=15)
	tamano = models.PositiveIntegerField()
	peso = models.PositiveIntegerField()
	color = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=50)
	fechaRescate = models.DateTimeField()
	estadoRescate = (('R','Rescatado'),('D','Disponible'),('A','Adoptado'))
	estado = models.CharField(max_length=1, choices=estadoRescate,default='D')