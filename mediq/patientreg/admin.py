from django.contrib import admin
from patientreg.models import Patientreg
class patientregadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','age','gender','hospital','doctor','message','phone')
admin.site.register(Patientreg,patientregadmin)