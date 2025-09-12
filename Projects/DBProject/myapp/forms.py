from django import forms
from .models import *

class Userform(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'