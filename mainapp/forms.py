from mainapp.models import  NivelCurso

from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from pycpfcnpj import cpfcnpj
from django.forms.widgets import ClearableFileInput

class NivelCursoForm(forms.ModelForm):

    class Meta:
        model = NivelCurso
        fields = '__all__'
