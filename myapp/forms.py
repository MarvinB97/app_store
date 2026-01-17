from django import forms


class CreateTask(forms.Form):
    title = forms.CharField(label='Titulo',max_length=200)
    description = forms.CharField(label='Descripcion', widget= forms.Textarea, max_length=500)
    cantidad = forms.IntegerField(label='Cantidad', max_value=15)

class CreateProject(forms.Form):
    name = forms.CharField(label='Nombre', max_length=20)
    description = forms.CharField(label='descripcion', widget=forms.Textarea, max_length=200)
