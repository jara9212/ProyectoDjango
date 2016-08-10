from django import forms
from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
        	'nombre',
        	'apellidos',
        	'edad',
        	'telefono',
        	'email',
        	'domicilio',
        ]
        labels = {
        	'nombre' : 'Nombre(s)',
            'apellidos' : 'Apellidos',
            'edad' : 'Edad',
            'telefono' : 'Telefono',
            'email' : 'Correo electronico',
            'domicilio' : 'Domicilio',
        }
        widgets = {
        	'nombre': forms.TextInput(attrs={'class':'form-control', 'id':'inputNombre', 'placeholder':'Nombre'}),
        	'apellidos': forms.TextInput(attrs={'class':'form-control', 'id':'inputApellidos', 'placeholder':'Apellidos'}),
        	'edad': forms.TextInput(attrs={'class':'form-control', 'id':'inputEdad', 'placeholder':'Edad'}),
        	'telefono': forms.TextInput(attrs={'class':'form-control', 'id':'inputTelefono', 'placeholder':'Telefono'}),
        	'email': forms.TextInput(attrs={'class':'form-control', 'id':'inputEmail', 'placeholder':'Email'}),
        	'domicilio': forms.TextInput(attrs={'class':'form-control', 'id':'inputDomicilio', 'placeholder':'Domicilio'}),
        }


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'numero_mascotas' : '# de Mascotas',
            'razones' : 'Razones',
        }
        widgets = {
            'numero_mascotas': forms.TextInput(attrs={'class':'form-control', 'id':'inputnMascotas', 'placeholder':'# de MAscotas'}),
            'razones': forms.Textarea(attrs={'class':'form-control', 'id':'inputRazones', 'placeholder':'Razones'}),
        }