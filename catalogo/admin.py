from django.contrib import admin
from catalogo.models import bicicleta, equipamiento

@admin.register(bicicleta)
class bicicletaAdmin(admin.ModelAdmin):
	list_display = ('marca', 'aro', 'precio',)

@admin.register(equipamiento)
class bicicletaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio',)
