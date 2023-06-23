from typing import Any, Dict
from django import forms
from .models import *
from django.contrib.auth.password_validation import validate_password

class TodoForm(forms.ModelForm):
    form_type = forms.CharField(widget=forms.HiddenInput(), initial='form1',label='')
    class Meta:
        model=TodoClass
        fields=['title','description']
        labels={
            "title":"task",
        }
class FinishTimeForm(forms.ModelForm):
    class Meta:
        model=FinishTimeClass
        fields=['finish_time']
        widgets = {
            'finish_time': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH-MM-SS'}),
        }
        

class NewPlayListForm(forms.ModelForm):
    form_type = forms.CharField(widget=forms.HiddenInput(), initial='form3',label='')
    class Meta:
        model = PlayListClass
        fields = ['title']
        labels={
            "title":"Playlist Name"
        }



    

        