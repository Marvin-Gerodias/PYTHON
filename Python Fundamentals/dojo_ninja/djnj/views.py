from django.shortcuts import render
from .models import Dojo, Ninja

def index(request):
    context = {
        "dojos" : Dojo.objects.all(),
        "ninjas" : Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def process(request):
    if request.POST['form'] == "Add_Dojo":
        Name = request.POST['name']
        City = request.POST['city']
        
        

# /////////////////////////////////////////////////////////////

# from django.shortcuts import render, HttpResponse, redirect
# from .models import Dojo, Ninja

# def index(request):
# 	context = {
# 		"dojos" : Dojo.objects.all(),
# 		"ninjas" : Ninja.objects.all()
# 	}
# 	return render(request, "index.html", context)


# def dojo(request):
#     dojo = Dojo()
#     if request.POST['form'] == "Add_Ninja":
#         firstname = request.POST['first_name']
#         lastname = request.POST['last_name']
#         dojostate = request.POST['dojo_select']
#         dojoget = Dojo.objects.get(id = dojostate)
#         Ninja.objects.create(first_name = firstname, last_name = lastname, dojoid = dojoget)

#     if request.POST['form'] == "Add_Dojo":
#         dojo.name = request.POST['name']
#         dojo.city = request.POST['city']
#         dojo.State = request.POST['state']
#         dojo.save()
#     return redirect("/")