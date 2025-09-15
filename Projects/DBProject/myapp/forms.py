from django import forms
from .models import *

class Userform(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model=userinfo
        fields=['name','email','dob','mobile']