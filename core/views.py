from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	data = {}
	template = "core/index.html"
	return render(request, template, data)