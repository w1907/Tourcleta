from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ArriendoForm
from catalogo.models import *

# Create your views here.

def crear_arriendo(request):
    if request.method == 'POST':
        form = ArriendoForm(request.POST)
        if form.is_valid():
            print("wachalomooooooox")
            form.save()
            return redirect(reverse('crear_arriendo')+"?ok")
    else:
        print("Holaaaaa")
        form = ArriendoForm()
    return render(request, "arriendo/arriendo.html", {'form':form})
