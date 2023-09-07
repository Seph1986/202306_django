from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("""marcador de posición para luego mostrar una lista
                         de todos los blogs""")


def new(request):
    return HttpResponse("""marcador de posición para mostrar un nuevo 
                        formulario para crear un nuevo blog""")


def create(request):
    return redirect("/")


def show(request, number):
    return HttpResponse(f"""marcador de posición para mostrar el número de 
                        blog: {number}""")


def edit(request,number):
    return HttpResponse(f"""marcador de posición para editar el blog {number} 
                        con un método llamado editar""")


def destroy(request, number):
    return redirect("/")

def keys(resquest):

    data={
        "llave" : "probando",
        "segunda": "prueba",
        "para_el": "profe"
    }

    return JsonResponse(data)