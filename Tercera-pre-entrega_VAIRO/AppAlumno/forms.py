from django import forms

class CuotaFormulario(forms.Form):
    cuota = forms.CharField()

class BuscaCuotaForm(forms.Form):
    cuota = forms.CharField()