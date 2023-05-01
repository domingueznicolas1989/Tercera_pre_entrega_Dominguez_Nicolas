from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfesorForm (forms.Form):
    nombre=forms.CharField(max_length=50, label = "Nombre ")
    apellido=forms.CharField(max_length=50, label = "Apellido ")
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)
    
class EstudianteForm (forms.Form):
    nombre=forms.CharField(max_length=50, label = "Nombre ")
    apellido=forms.CharField(max_length=50, label = "Apellido ")
    email=forms.EmailField()
    
class CursoForm (forms.Form):
    nombre=forms.CharField(max_length=50, label = "Nombre ")
    comision=forms.CharField(max_length=50, label = "Comision ")
    
