from django.contrib import admin
from .models import Terminal, Anden, Empresa, Bus, UsuarioTerminal, BusEstacionado

# Modelo de Andenes con detalles del Terminal y Andén
class AndenInline(admin.TabularInline):
    model = Anden
    extra = 1

# Modelo Principal de Terminales con inclusión de InLine de Andenes
class TerminalAdmin(admin.ModelAdmin):
    inlines = [AndenInline]

# Clase Administrativa para Andenes
class AndenAdmin(admin.ModelAdmin):
    list_display = ('numero', 'terminal')
    search_fields = ('numero', 'terminal__nombre')

# Clase Administrativa para Empresas con el modo de Filtrado
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'terminal')
    search_fields = ('nombre', 'terminal__nombre')

# Clase Administrativa para Buses
class BusAdmin(admin.ModelAdmin):
    list_display = ('numero_placa', 'empresa', 'estado')
    search_fields = ('numero_placa', 'empresa__nombre')

# Clase Administrativa para Usuarios Terminal
class UsuarioTerminalAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'terminal')
    search_fields = ('usuario__username', 'terminal__nombre')

# Clase Administrativa para Buses Estacionados
class BusEstacionadoAdmin(admin.ModelAdmin):
    list_display = ('bus', 'llegada', 'salida', 'multa')
    search_fields = ('bus__numero_placa',)

models_to_register = [
    (Terminal, TerminalAdmin),
    (Anden, AndenAdmin),
    (Empresa, EmpresaAdmin),
    (Bus, BusAdmin),
    (UsuarioTerminal, UsuarioTerminalAdmin),
    (BusEstacionado, BusEstacionadoAdmin)
]

for model, model_admin in models_to_register:
    try:
        admin.site.register(model, model_admin)
    except admin.sites.AlreadyRegistered:
        pass
