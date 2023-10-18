from django import forms



class CuotaFormulario(forms.Form):
    cuota = forms.CharField()
    importe_a_pagar = forms.IntegerField()


class MateriaFormulario(forms.Form):
    materia = forms.CharField()
    Nota_primer_parcial = forms.IntegerField()
    Nota_segundo_parcial = forms.IntegerField()
    Nota_del_final = forms.IntegerField()



class FinalFormulario(forms.Form):
    final = forms.CharField()  








        
       




   


