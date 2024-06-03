from django import forms
from docreg.models import Docreg
from django.core.exceptions import ValidationError

class docregisterr(forms.ModelForm):
    class Meta:
        model = Docreg
        fields = ['fullname','gender','dob','languages','nationality','contactNumber',
                  'email','password','medicalDegree','licenseNumber','specialization','experience',
    'workplace','workAddress','workContact','workEmail','photo', 'monday_start', 'monday_end',
                 'tuesday_start', 'tuesday_end', 'wednesday_start', 'wednesday_end',
             'thursday_start', 'thursday_end','friday_start', 'friday_end', 'saturday_start','saturday_end',
            'sunday_start','sunday_end']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Docreg.objects.filter(email=email).exists():
            raise ValidationError("This email address is already registered.")
        return email

class docloginn(forms.Form):
    email = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())