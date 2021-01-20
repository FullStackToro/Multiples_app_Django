from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def indice(request):
    return HttpResponse("marcador de posición para luego mostrar una lista de todos los blogs")

def nuevo(request):
    return HttpResponse("marcador de posición para mostrar un nuevo formulario para crear un nuevo blog")

def crear(request):
    return redirect('/blogs')

def show(request,my_val):
    return HttpResponse(f"marcador de posición para mostrar el número de blog: {my_val}")

def editar(request, my_val):
    return HttpResponse(f"marcador de posición para editar el blog {my_val}")

def destruir(request, my_val):
    return redirect('/blogs')