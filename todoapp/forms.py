from django import forms
from .models import task

class taskform(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title','description','date','time','task_status','priority']
        weidgets ={
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }