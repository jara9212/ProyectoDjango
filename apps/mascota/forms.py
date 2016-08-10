from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
        	'nombre',
        	'edad_aproximada',
        	'sexo',
        	'fecha_rescate',
        	'persona',
        	'vacuna',
        ]
        labels = {
        	'nombre': 'Nombre',
        	'edad_aproximada': 'Edad aproximada',
        	'sexo': 'Sexo',
        	'fecha_rescate': 'Fecha de rescate',
        	'persona': 'Adoptante',
        	'vacuna': 'Vacunas',
        }
        widgets = {
        	'nombre': forms.TextInput(attrs={'class':'form-control', 'id':'inputNombre', 'placeholder':'Nombre'}),
        	'edad_aproximada': forms.TextInput(attrs={'class':'form-control', 'id':'inputEdad', 'placeholder':'Edad'}),
        	'sexo': forms.TextInput(attrs={'class':'form-control', 'id':'inputSexo', 'placeholder':'Sexo'}),
        	'fecha_rescate': forms.DateTimeInput(attrs={'class':'form-control', 'id':'inputFecha', 'placeholder':'Fecha de rescate'}),
        	'persona': forms.Select(attrs={'class':'form-control', 'id':'inputFecha'}),
        	'vacuna': forms.CheckboxSelectMultiple(),
        }