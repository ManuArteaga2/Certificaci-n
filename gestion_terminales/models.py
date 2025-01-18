from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime

class Terminal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Terminal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Anden(models.Model):
    ESTADO_CHOICES = [
        ('ocupado', 'Ocupado'),
        ('disponible', 'Disponible'),
        ('mantenimiento', 'Mantenimiento'),
    ]
    numero = models.CharField(max_length=10)
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='disponible')

    def __str__(self):
        return f"Anden {self.numero} - {self.terminal.nombre}"

    def disponible(self):
        return self.estado == 'disponible'


class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name='empresas')

    def __str__(self):
        return self.nombre

class Bus(models.Model):
    numero_placa = models.CharField(max_length=10, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='buses')
    estado = models.CharField(max_length=20, choices=[('estacionado', 'Estacionado'), ('en ruta', 'En Ruta')])
    tiempo_max_permitido = models.IntegerField()  # En minutos
    anden = models.ForeignKey(Anden, null=True, blank=True, on_delete=models.SET_NULL)
    tiempo_excedido = models.DurationField(null=True, blank=True)
    hora_llegada = models.DateTimeField(null=True, blank=True)
    hora_salida = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.estado == 'estacionado' and self.tiempo_max_permitido:
            tiempo_actual = datetime.now()
            tiempo_actual = self.updated_at if self.updated_at else tiempo_actual
            self.tiempo_excedido = timedelta(minutes=max(0, (self.tiempo_max_permitido - (tiempo_actual - self.created_at).total_seconds() / 60)))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero_placa

class UsuarioTerminal(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

class BusEstacionado(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    llegada = models.DateTimeField()
    salida = models.DateTimeField(null=True, blank=True)
    multa = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.bus.numero_placa} - Llegada: {self.llegada}"
