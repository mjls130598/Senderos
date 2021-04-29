from django import forms

class ComentarioForm(forms.Form):
    autor = forms.CharField(label='Autor', max_length=100, required= True)
    contenido = forms.CharField(max_length=500,required= True)

class ExcursionForm(forms.Form):
    nombre = forms.CharField(label='Título', max_length=120, required=True)
    descripcion = forms.CharField(label='Descripción de la ruta', max_length = 1000, required=True)
    tags = forms.CharField(label= 'Etiquetas', max_length=120, required=True)
    fotos = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    pie = forms.CharField(label='Pie de foto', max_length=100)