from django import forms
from .models import Contact

class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['username', 'email', 'mobile', 'feedback']