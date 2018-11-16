from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	data = {}
	template = "core/index.html"
	print(request.POST)
	return render(request, template, data)

def index_usuario(request):
	data = {}
	template = "core/index_usuario.html"
	return render(request, template, data)

def index_empleado(request):
	data = {}
	template = "core/index_empleado.html"
	return render(request, template, data)

def index_admin(request):
	pass