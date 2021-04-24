from django.shortcuts import render, HttpResponse

def index(request):
    print(request.session.items())
    return render(request, "index.html")

