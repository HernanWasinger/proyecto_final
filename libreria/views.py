from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.decorators import login_required
def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')
def libros(request):
    libros = Libro.objects.all()   
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    if request.user.is_authenticated:
        formulario = LibroForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('libros')
        return render(request, 'libros/crear.html', {'formulario': formulario})
    return redirect('login')

def editar(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        libro = Libro.objects.get(id=id)
        formulario = LibroForm(request.POST or None, request.FILES or None, instance= libro)
        if formulario.is_valid() and request.POST:
            formulario.save()
            return redirect('libros')
        return render(request, 'libros/editar.html', {'formulario': formulario})
    return redirect('inicio')

def eliminar(request, id): 
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

