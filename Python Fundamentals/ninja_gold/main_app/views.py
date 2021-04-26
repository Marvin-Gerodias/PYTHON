from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []

        
    return render(request, "index.html")
    
def process(request):
    if 'gold' in request.session and request.POST['form'] == 'farm':
        rand_gold = random.randint(10,20)
        print(rand_gold)
        request.session['gold'] += rand_gold
        print(request.session['gold'])
        request.session['log'].append(rand_gold)
        if len(request.session['log']) > 4:
            request.session['log'].pop(0)

    elif 'gold' in request.session and request.POST['form'] == 'cave':
        rand_gold = random.randint(5,10)
        print(rand_gold)
        request.session['gold'] += rand_gold
        print(request.session['gold'])
        request.session['log'].append(rand_gold)
        if len(request.session['log']) > 4:
            request.session['log'].pop(0)

    elif 'gold' in request.session and request.POST['form'] == 'house':
        rand_gold = random.randint(2,5)
        print(rand_gold)
        request.session['gold'] += rand_gold
        print(request.session['gold'])
        request.session['log'].append(rand_gold)
        if len(request.session['log']) > 4:
            request.session['log'].pop(0)

    elif 'gold' in request.session and request.POST['form'] == 'casino':
        rand_gold = random.randint(-50,50)
        print(rand_gold)
        request.session['gold'] += rand_gold
        print(request.session['gold'])
        request.session['log'].append(rand_gold)
        if len(request.session['log']) > 4:
            request.session['log'].pop(0)


    return render(request, "index.html")

def clear(request):
    request.session.flush()
    return redirect('/')