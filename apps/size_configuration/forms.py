from django import forms

from .models import Size
class Size_Form(forms.ModelForm):
    class Meta:
        model = Size
        fields = [            
            'code',
            'gender',
            'description',        
            'body_area',  
        ]
        labels = {            
            'code' : 'Code', 
            'gender' : 'Gender',
            'description' : 'Description',
            'body_area':  'Protection Area',    
        }
        widgets = {
            'code' : forms.TextInput(attrs={'class':'form-control'}),   
            'gender' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),            
            'body_area' : forms.Select(attrs={'class':'form-control'}),    
        }

