from django.forms import ModelForm
from .models import Product,Supplier

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

