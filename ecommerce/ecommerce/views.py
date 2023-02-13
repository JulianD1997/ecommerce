from django.shortcuts import render
from inventory.models import Product

def index(request):
    column_names = []
    fields = Product._meta.get_fields()
    _titles = [field.get_attname_column()[1] for field in fields]
    
    for title in _titles:
        
        if 'id' == title:
            continue
        
        column_names.append(title.replace('_id',''))
    
    if (request.GET.get('search')):
        products = Product.objects.filter(name__icontains = request.GET.get('search'))
        
    else:
        products = Product.objects.all()
        
    context = {
        'products':products,
        'column_names':column_names
    }
    
    return render(request,'index.html',context)