from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('<letter>',views.index, name='index'),
    path('',include('inventory.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
