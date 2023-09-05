from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.

def root(request):
    return redirect("/blogs")


def index(request):
    return HttpResponse("""Placeholder para luego mostrar una lista de todos
                        los blogs""")


def new(request):
    return HttpResponse("""Placeholder para mostrar un nuevo formulario para
                        crear un nuevo blog""")


def create(request):
    return redirect("/")


def show(request, number):
    return HttpResponse(f"Placeholder para mostrar el blog numero: {number}")


def edit(request,number):
    return HttpResponse(f"Placeholder para editar el blog {number}")


def destroy(request, number):
    return redirect("/")

def keys(resquest):

    data={
        "llave" : "probando",
        "segunda": "prueba",
        "para_el": "profe"
    }

    return JsonResponse(data)