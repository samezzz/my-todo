from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['due_date', 'due_time']
        labels = {'due_time': ''}
        widgets = {
            'due_date': AdminDateWidget(attrs={'type':'date'}),
            'due_time': AdminTimeWidget(attrs={'type':'time'}),
        }
    
