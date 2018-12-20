from django import forms
from app.models import Usuario, Tiempo, Estilo, Artista, Discografica
from django.forms import ModelForm

class Select_Form (forms.Form):
    userName = forms.ModelChoiceField(Usuario.objects.all())
    

 
            
    