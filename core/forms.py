from django import forms
from .models import tabla

class tablaForm(forms.ModelForm):
    class Meta:
        model = tabla
        fields = ['tabla']