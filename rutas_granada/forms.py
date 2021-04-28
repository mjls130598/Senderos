from django import forms

class ComentarioForm(forms.Form):
    autor = forms.CharField(label='Autor', max_length=100)
    contenido = forms.CharField(label='Comentario', max_length=500)