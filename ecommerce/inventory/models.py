from django.db import models
from datetime import date
# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50,null=False)
    stock = models.IntegerField(default=20)
    price_unit = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name='supplier')
    
    def __str__(self):
        return self.name
    
