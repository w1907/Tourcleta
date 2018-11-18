from django.db import models
from catalogo.models import Bicicleta, Equipamiento
from django.contrib.auth.models import User


# Create your models here.

class Arriendo(models.Model):
    a_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    a_bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE, null=True)
    a_equipamiento = models.ForeignKey(Equipamiento, on_delete=models.CASCADE, null=True)
    participantes = models.PositiveIntegerField()
    duracion = models.PositiveIntegerField()






