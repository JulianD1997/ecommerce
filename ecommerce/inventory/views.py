from django.shortcuts import render
from .models import Product,Supplier
from .forms import ProductForm,SupplierForm

def add_product(request): 
    form = ProductForm()
    context = {
        'form':form,
        'accion':'Agregar producto',
    }
    return render(request,'product/form_product.html',context)

def add_supplier(request):
    return render(request,'supplier/add_supplier.html',{})

def edit_product(request,id):
    if(request.method == 'GET'):
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product)
        context = {
            'accion':'Editar producto',
            'form':form,
        }
        return render(request,'product/form_product.html',context)