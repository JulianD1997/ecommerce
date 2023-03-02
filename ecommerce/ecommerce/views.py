from asyncio.windows_events import NULL
from django.contrib import messages
from django.shortcuts import render
from inventory.models import Product,Supplier

def index(request, letter = NULL):
    column_names = []
    fields = Product._meta.get_fields()
    _titles = [field.get_attname_column()[1] for field in fields]
    for title in _titles:
        if 'id' == title:
            continue
        column_names.append(title.replace('_id',''))
    abc = list(map(chr, range(97, 123)))    
    if letter != NULL:
        products = Product.objects.filter(name__istartswith=letter)
        context = {
        'abc':abc,
        'products':products,
        'column_names':column_names
        }
        return render(request,'index.html',context)
    products = Product.objects.all()
    context = {
        'abc':abc,
        'products':products,
        'column_names':column_names
    }
    try:
        if (request.GET.get('search')):
            products = Product.objects.filter(name__icontains = request.GET.get('search'))   
        elif request.GET.get('order'):
            products = Product.objects.all().order_by(request.GET.get('order'))

            if request.GET.get('order') == 'supplier':
                    products = Product.objects.all().order_by('supplier__name')
    except :
        products = Product.objects.all().order_by('name')
       
    context = {
        'abc':abc,
        'products':products,
        'column_names':column_names
    }
    return render(request,'index.html',context)