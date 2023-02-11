from django.shortcuts import render
from .models import Product

def add_product(request):
    return render(request,'product/add_product.html',{})
def add_supplier(request):
    return render(request,'supplier/add_supplier.html',{})

