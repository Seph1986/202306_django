from django.shortcuts import redirect, HttpResponse

# Create your views here.
def register(request):

    return HttpResponse("marcador de posición para que los usuarios creen un nuevo registro de usuario")


def login(request):

    return HttpResponse("marcador de posición para que los usuarios inicien sesión")


def users(request):

    return HttpResponse("marcador de posición para luego mostrar toda la lista de usuarios")