from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


# def root_method(request):
#     return redirect('/blogs') 

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs.")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog.")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse(f"Placeholder {num}")

def edit(request, num):
    return HttpResponse(f"Placeholder to edit blog {num}")

def destroy(request):
    return redirect('/blogs')

def jsonresponse(request):
    return JsonResponse({"response": "JSON response from jsonresponse", "status": True})



