from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
		]
		fields = {
				'username' : 'Nombre de usuario',
				'first_name' : 'Nombre(s)',
				'last_name' : 'Apellidos',
				'email' : 'Correo',
		}

		# widgets = {
  #       	'username': forms.TextInput(attrs={'class':'form-control', 'id':'inputUser', 'placeholder':'username'}),
  #       	'firstname': forms.TextInput(attrs={'class':'form-control', 'id':'inpuNombre', 'placeholder':'Nombre(s)'}),
  #       	'lastname': forms.TextInput(attrs={'class':'form-control', 'id':'inputApe', 'placeholder':'Apellidos'}),
  #       	'email': forms.TextInput(attrs={'class':'form-control', 'id':'inputEmail', 'placeholder':'Email'}),
  #       }