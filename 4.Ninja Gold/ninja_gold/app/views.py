from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'message' not in request.session:
        request.session['message'] = []

    return render(request,'index.html')


def farm(request):
    
    random_gold = random.randint(10,20)
    request.session['gold'] += random_gold
    request.session['message'].insert(0, f'Guau ! You have won {random_gold}, Farm')

    return redirect('/')

def cave(request):
    
    random_gold = random.randint(5,10)
    request.session['gold'] += random_gold
    request.session['message'].insert(0, f'Guau ! You have won {random_gold}, Cave')

    return redirect('/')

def house(request):
    
    random_gold = random.randint(2,5)
    request.session['gold'] += random_gold
    request.session['message'].insert(0, f'Guau ! You have won {random_gold}, House')

    return redirect('/')


def casino(request):

    dice = random.randint(1,6)

    if dice < 1:
        random_gold = random.randint(0,50)
        request.session['gold'] += random_gold
        request.session['message'].insert(0, f'Guau ! You have won {random_gold}, Casino')
    else:
        random_gold = random.randint(0,50)
        request.session['gold'] -= random_gold
        request.session['message'].insert(0, f'Ufff ! You lost {random_gold}, Casino')
    

    return redirect('/')


def clear(request):

    request.session.clear()

    return redirect('/')