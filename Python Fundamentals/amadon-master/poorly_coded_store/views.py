from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all(),
    }


    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    id_from_form = Product.objects.get(id = request.POST["id"])
    total_charge = quantity_from_form * id_from_form.price
    print("Charging credit card...")
    
    newOrder = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    id = newOrder.id
    product_id = Product.price
    print(product_id)
    
    return redirect(f"/process/{id}")



def process(request, id):

    total_sum = 0
    total_quantity = 0
    for i in Order.objects.all():
        total_sum += i.total_price
        total_quantity += i.quantity_ordered

    print(total_sum)
    print(total_quantity)

    context = {
        "totalSum" : total_sum,
        "totalQuantity" : total_quantity,
        "newOrder" : Order.objects.get(id=id),
    }

    return render(request, "store/checkout.html", context)

