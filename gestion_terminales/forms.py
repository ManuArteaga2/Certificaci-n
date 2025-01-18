from django import forms
from .models import Bus, Anden

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['numero_placa', 'empresa', 'estado', 'tiempo_max_permitido', 'anden', 'hora_llegada', 'hora_salida']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['anden'].queryset = Anden.objects.filter(estado='disponible')
