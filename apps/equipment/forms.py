from django import forms

from .models import Equipment, Work_Activities

class Equipment_Form(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [            
            'code',
            'name',
            'description',        
            'time_of_life',  
            'manteinance_cleaning',
            'certification',
            'mode_use',
            'start_date',
            'end_date',
            'body_area',
            'element_classification',
            'work_activities',
        ]
        labels = {            
            'code' : 'Code',
            'name' : 'Name',
            'description' : 'Description',        
            'time_of_life' : 'Time of life',  
            'manteinance_cleaning' : 'Manteinance Cleaning',
            'certification' : 'Certification',
            'mode_use' : 'Mode Use',
            'start_date' : 'Start Date',
            'end_date' : 'End Date',   
            'body_area' : 'Body Area',
            'element_classification' : 'Element Classification',
            'work_activities' : 'Work Activities',
        }
        widgets = {
            'code' : forms.TextInput(attrs={'class':'form-control'}),   
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'manteinance_cleaning' : forms.TextInput(attrs={'class':'form-control'}),
            'certification' : forms.TextInput(attrs={'class':'form-control'}),
            'mode_use' : forms.TextInput(attrs={'class':'form-control'}),
            'time_of_life': forms.DateInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.DateInput(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control'}),            
            'end_date' : forms.Select(attrs={'class':'form-control'}),
            'body_area' : forms.Select(attrs={'class':'form-control'}),
            'element_classification' : forms.Select(attrs={'class':'form-control'}),  
            'work_activities' : forms.Select(attrs={'class':'form-control js-example-tags','multiple' : 'multiple'}),  
        }