from django import forms
from .models import BodyPart
class Body_Part_Form(forms.ModelForm):
    class Meta:
        model = BodyPart
        fields = [
            'code',
            'name',
            'description',            
        ]
        labels = {
            'code' : 'Code',
            'name' : 'Name',
            'description' : 'Description', 
        }
        widgets = {
            'code' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}), 
        }