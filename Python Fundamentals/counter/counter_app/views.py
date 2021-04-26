from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if 'number' in request.session:
        request.session['number'] += 1
    else:
        request.session['number'] = 1

    return render(request, 'index.html')

def destroy(request):
    del request.session['counter']
    return redirect('/')

def add2(request):
    if 'number' in request.session:
        request.session['number'] += 2
    else:
        request.session['number'] = 1

    return render(request, 'index.html')
