from django.contrib import admin
from patientreg.models import Patientreg
class patientregadmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','age','gender','password','address','message','phone','photo')
admin.site.register(Patientreg,patientregadmin)