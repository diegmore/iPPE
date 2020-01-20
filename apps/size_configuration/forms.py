from django import forms

from .models import Size
from apps.body_configuration.models import BodyPart
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

    def __init__(self,*args,**kwargs):
        super(Size_Form,self).__init__(*args,**kwargs)
        self.fields['body_area'].queryset=BodyPart.objects.filter(status=True)
        