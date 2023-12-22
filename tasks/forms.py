from django import forms
from .models import Task
from django.forms import ModelForm

#aca define el formulario para crear la tardea
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','descriptio','important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'descriptio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloque una descripcion'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input text-center'}),
        }
