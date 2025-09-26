from django import forms
from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model=Usersignup
        fields='__all__'
        
class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','category','notesfile','desc']