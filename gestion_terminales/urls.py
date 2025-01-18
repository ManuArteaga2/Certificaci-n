from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  
from gestion_terminales import views  

app_name = 'gestion_terminales'

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('gestion_empresas/', views.gestion_empresas, name='gestion_empresas'),
    path('terminales/', views.lista_terminales, name='lista_terminales'),
    path('gestion_buses/', views.gestion_buses, name='gestion_buses'),
    path('registrar_bus/', views.registrar_bus, name='registrar_bus'),
    path('editar_bus/<int:bus_id>/', views.editar_bus, name='editar_bus'),  # Cambio de Expresiones Regulares a Path()
    path('eliminar_bus/<int:bus_id>/', views.eliminar_bus, name='eliminar_bus'),
    path('reporte_diario/', views.reporte_diario, name='reporte_diario'),
    path('login/', auth_views.LoginView.as_view(template_name='gestion_terminales/inicio_sesion.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),  # Ruta al panel de administración
    path('cuentas/', include('django.contrib.auth.urls')),  # URLs de autenticación de Django
]
