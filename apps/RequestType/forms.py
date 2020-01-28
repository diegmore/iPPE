from django import forms
from .models import Request_Type


class Request_Type_Form(forms.ModelForm):
    class Meta:
        model = Request_Type
        fields = [
            'code',
            'name',
            'detail',
            'status', 
            'element_type', 
        ]
        labels = {
            'code' : 'codigo',
            'name' : 'Nombre',
            'detail' : 'Descripcion', 
            'status' : 'estado',  
            'element_type' :  'tipo de elemento',            
        }
        widgets = {
            'code' : forms.TextInput(attrs={'class':'form-control col-sm-3 col-md-6 col-lg-12'}),
            'name' : forms.TextInput(attrs={'class':'form-control col-sm-3 col-md-6 col-lg-12'}),
            'detail' : forms.Textarea(attrs={'class':'form-control col-sm-3 col-md-6 col-lg-12'}), 
            'status' :  forms.CheckboxInput(),
            'element_type' : forms.Select(attrs={'class':'form-control col-sm-3 col-md-6 col-lg-12'}),
        }



