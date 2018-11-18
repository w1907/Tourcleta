from django.contrib import admin
from catalogo.models import Bicicleta, Equipamiento
from arriendo.models import Arriendo


@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
	list_display = ('a_bicicleta', 'a_equipamiento', 'participantes', 'duracion')

