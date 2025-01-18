from django.contrib import admin  
from django.urls import path, include
from gestion_terminales import views  

urlpatterns = [
    path('admin/', admin.site.urls),  # ruta del panel
    path('gestion_terminales/', include('gestion_terminales.urls')),
    path('', views.home, name='home'),  # Ruta de la página principal
    path('cuentas/', include('django.contrib.auth.urls')),  # URLs de autenticación de Django
]
