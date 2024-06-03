from django import forms
from hospreg.models import Hospreg

class hospregisterr(forms.ModelForm):
    class Meta:
        model = Hospreg
        fields = ['hospital_name','hospital_type','email','phone','address','license','city','password','confirm_password','photo'] 
        widgets = {
            'password': forms.PasswordInput(),
        }

class hosploginn(forms.Form):
    email = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())