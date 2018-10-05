from django import forms
from .models import *

class UbicacionForm(forms.ModelForm):
	class Meta:
			model = Profesionales
			fields = ('profesion','ciudad')
