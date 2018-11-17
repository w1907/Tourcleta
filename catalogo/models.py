from django.db import models

class bicicleta(models.Model):
	marca = models.CharField(max_length=20, null=True)
	aro = models.IntegerField(null=True)
	precio = models.IntegerField(null=True)
	imagen_bicicleta = models.ImageField(upload_to = 'imagenes_bicicletas', null=True, blank=True)

	def __str__(self):
		return "marca:'%s', aro:'%s', precio:'%s', self:'%s'" % (self.marca, self.aro, self.precio, self.imagen_bicicleta)

class equipamiento(models.Model):
	nombre = models.CharField(max_length=20, null=True)
	precio = models.IntegerField(null=True)
	imagen_equipamiento = models.ImageField(upload_to = 'imagenes_equipamiento', null=True, blank=True)

	def __str__(self):
		return self.nombre