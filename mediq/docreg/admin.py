from django.contrib import admin
from docreg.models import Docreg
class docregadmin(admin.ModelAdmin):
    list_display=('fullname','gender','dob','languages','nationality','contactNumber',
                  'email','medicalDegree','licenseNumber','specialization','experience',
    'workplace','workAddress','workContact','workEmail')
admin.site.register(Docreg,docregadmin)
