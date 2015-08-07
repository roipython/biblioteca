from django import forms

class Autor_Update(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellidos = forms.CharField(max_length=40)
    email = forms.EmailField()
