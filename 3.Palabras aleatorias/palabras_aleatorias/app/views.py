from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def random_word(request):
    
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1


    request.session['ran_word'] = get_random_string(length=32)

    return render(request, 'index.html')

def clear(request):

    request.session.clear()

    return redirect('/random_word')