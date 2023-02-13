from django.urls import path,include
from . import views
urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
]
