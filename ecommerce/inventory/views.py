from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Product,Supplier
from .forms import ProductForm,SupplierForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ProductForm()
    context = {
        'accion':"{% url 'add_product' %}",
        'form':form,
        'method':'POST',
        'title':'Agregar producto',        
    }
    
    return render(request,'product/form_product.html',context)

def edit_product(request,id):
    product = Product.objects.get(id=id)
    
    if(request.method == 'POST'):
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            context = {
                'accion':"{% url 'edit_product' id=id %}",
                'id':id,
                'form':form,
                'method':'POST',
                'title':'Editar producto',
            }
            messages.success(request, 'El producto fue modificado')
            return render(request,'product/form_product.html',context)
    
    form = ProductForm(instance=product)
    context = {
        'accion':"{% url 'edit_product' id=id %}",
        'id':id,
        'form':form,
        'method':'POST', 
        'title':'Editar producto',
    }
    return render(request,'product/form_product.html',context)

def delete_product(request,id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('index')

def add_supplier(request):
    if request.method =='POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = SupplierForm()
    context = {
        'title': 'Agregar Proveedor',
        'form': form,
    }
    return render(request,'supplier/form_supplier.html',context)

