from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import bicicleta, equipamiento

def catalogo(request, tipo_catalogo):
	data = {}
	template = "catalogo.html"
	data['catalogo'] = tipo_catalogo
	if tipo_catalogo == "bicicleta":
		bicicletas = bicicleta.objects.all()
		data['objetos'] = bicicletas
	elif tipo_catalogo == "equipamiento":
		equipamientos = equipamiento.objects.all()
		data['objetos'] = equipamientos

	return render(request, template, data)

def ver_mas(request, tipo_catalogo, ver_mas, pk):
	data = {}
	template = "ver_mas.html"
	data['ver_mas'] = tipo_catalogo
	if tipo_catalogo == "bicicleta":
		bicicletas = bicicleta.objects.get(id=pk)
		data['objetos'] = bicicletas
	elif tipo_catalogo == "equipamiento":
		equipamientos = equipamiento.objects.get(id=pk)
		data['objetos'] = equipamientos
	return render(request, template, data)
	