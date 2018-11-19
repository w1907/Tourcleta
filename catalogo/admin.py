from django.contrib import admin
from catalogo.models import Bicicleta, Equipamiento, Sede
"""
@admin.register(Bicicleta)
class BicicletaAdmin(admin.ModelAdmin):
	list_display = ('marca', 'aro', 'precio','imagen_bicicleta',)
"""
admin.site.register(Bicicleta)
admin.site.register(Sede)

@admin.register(Equipamiento)
class BicicletaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio',)
