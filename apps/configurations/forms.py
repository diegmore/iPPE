from django import forms

from .models import Element_Type,Element_Classification
class Element_Type_Form(forms.ModelForm):
    class Meta:
        model = Element_Type
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
class Element_Classification_Form(forms.ModelForm):
    class Meta:
        model = Element_Classification
        fields = [
            'code',
            'name',
            'description',
            'element_type',            
        ]
        labels = {
            'code ':  'Code',
            'name' : 'Name',
            'description' : 'Description', 
            'element_type' : 'Element Type', 
        }
        widgets = {
            'code' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'element_type' : forms.Select(attrs={'class':'form-control'}), 
        }