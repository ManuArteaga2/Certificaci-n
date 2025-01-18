from django.shortcuts import render, get_object_or_404, redirect
from .models import Terminal, Anden, Empresa, Bus
from .forms import BusForm
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required, user_passes_test
from .utils import es_administrador 

def lista_terminales(request):
    terminales = Terminal.objects.all()
    contexto = {'terminales': terminales}
    return render(request, 'gestion_terminales/lista_terminales.html', contexto)

def home(request):
    es_admin = request.user.groups.filter(name='Administrador').exists()
    contexto = {'es_admin': es_admin}
    return render(request, 'gestion_terminales/home.html', contexto)

def gestion_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'gestion_terminales/gestion_empresas.html', {'empresas': empresas})

def gestion_buses(request):
    buses = Bus.objects.all()
    if 'nro_placa' in request.GET:
        buses = buses.filter(numero_placa__icontains=request.GET['nro_placa'])
    if 'empresa' in request.GET:
        buses = buses.filter(empresa__nombre__icontains=request.GET['empresa'])
    if 'estado' in request.GET:
        buses = buses.filter(estado__icontains=request.GET['estado'])
    
    return render(request, 'gestion_terminales/gestion_buses.html', {'buses': buses})

def registrar_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            bus = form.save(commit=False)
            if bus.estado == 'estacionado' and bus.anden and bus.anden.disponible():
                bus.hora_llegada = timezone.now()
                bus.anden.estado = 'ocupado'
                bus.anden.save()
                bus.save()
                return redirect('gestion_terminales:gestion_buses')
            else:
                form.add_error('anden', 'El andén seleccionado no está disponible.')
    else:
        form = BusForm()
    return render(request, 'gestion_terminales/registrar_bus.html', {'form': form})

def editar_bus(request, bus_id):
    bus = get_object_or_404(Bus, pk=bus_id)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            if form.cleaned_data['estado'] == 'estacionado' and form.cleaned_data['anden'] and form.cleaned_data['anden'].disponible():
                bus.hora_salida = timezone.now()
                form.cleaned_data['anden'].estado = 'ocupado'
                form.cleaned_data['anden'].save()
            form.save()
            return redirect('gestion_terminales:gestion_buses')
    else:
        form = BusForm(instance=bus)
    return render(request, 'gestion_terminales/editar_bus.html', {'form': form})

def eliminar_bus(request, bus_id):
    bus = get_object_or_404(Bus, pk=bus_id)
    if request.method == 'POST':
        bus.anden.estado = 'disponible'
        bus.anden.save()
        bus.delete()
        return redirect('gestion_terminales:gestion_buses')
    return render(request, 'gestion_terminales/eliminar_bus.html', {'bus': bus})

@login_required
@user_passes_test(es_administrador)
def reporte_diario(request):
    es_admin = es_administrador(request.user)
    today = timezone.now().date()
    buses = Bus.objects.filter(hora_llegada__gte=today, hora_llegada__lt=today + timedelta(days=1))
    contexto = {'buses': buses, 'es_admin': es_admin}
    return render(request, 'gestion_terminales/reporte_diario.html', contexto)
