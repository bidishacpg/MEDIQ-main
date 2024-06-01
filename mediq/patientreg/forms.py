from django import forms
from patientreg.models import Patientreg

class patregisterr(forms.ModelForm):
    class Meta:
        model = Patientreg
        fields = ['first_name','last_name','email','age','gender','password','address','message','phone','photo']
        widgets = {
            'password': forms.PasswordInput(),
        }
        

class patloginn(forms.Form):
    email = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())