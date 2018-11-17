from django.db import models

class bicicleta(models.Model):
	marca = models.CharField(max_length=20, null=True)
	aro = models.IntegerField(null=True)
	precio = models.IntegerField(null=True)

class equipamiento(models.Model):
	nombre = models.CharField(max_length=20, null=True)
	precio = models.IntegerField(null=True)