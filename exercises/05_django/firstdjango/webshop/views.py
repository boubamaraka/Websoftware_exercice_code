from django.http import HttpResponse, Http404,HttpResponseNotFound
from django.shortcuts import render,render_to_response
from webshop.models import Product

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    #product=Product.objects.get(pk=product_id)
    try:
         product=Product.objects.get(pk=product_id)
         return render_to_response("webshop/product_view.html",{'product':product})
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def available_products(request):
    products=Product.objects.filter(quantity__gt=0)

    return render_to_response("webshop/product_list.html",{"products":products})
