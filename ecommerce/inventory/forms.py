from django.forms import ModelForm, TextInput,NumberInput,Textarea,Select
from django.utils.translation import gettext_lazy as _
from .models import Product,Supplier

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        
        fields = ('name','stock','price_unit','description','supplier')
        
        labels ={
            'name': _('Nombre del producto'),
            'stock': _('Cantidad total del producto'),
            'price_unit':_('Precio por unidad'),
            'description':_('Descripcion del producto'),
            'supplier':_('Proveedor')
        }
        widgets ={
            'name': TextInput(attrs={'class':'form__input'}),
            'stock': NumberInput(attrs={'class':'form__input'}),
            'price_unit':NumberInput(attrs={'class':'form__input'}),
            'description':Textarea(attrs={'class':'form__area'}),
            'supplier':Select(attrs={'class':'form__select'})
        }
