from django import forms
from .models import Video 

class VideForm(forms.ModelForm):
    class Meta:
        model=Video 
        fields={'title','desc','video','img'}