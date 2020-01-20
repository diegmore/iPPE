from django import forms

from .models import Warehouse
class Warehouse_Form(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = [
            'name',
            'location',
            'addres', 
            'phone_number',           
        ]
        labels = {
            'name' : 'Name',
            'location' : 'Location',
            'addres' : 'Addres', 
            'phone_number' : 'Phone Number', 
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'location' : forms.Select(attrs={'class':'form-control'}),
            'addres' : forms.TextInput(attrs={'class':'form-control'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control'}),
        }