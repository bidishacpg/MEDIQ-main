from django.contrib import admin
from docreg.models import Docreg
class docregadmin(admin.ModelAdmin):
    list_display=('id','fullname','gender','dob','languages','nationality','contactNumber',
                  'email','password','medicalDegree','licenseNumber','specialization','experience',
    'workplace','workAddress','workContact','workEmail','photo', 'monday_start', 'monday_end',
                 'tuesday_start', 'tuesday_end', 'wednesday_start', 'wednesday_end',
             'thursday_start', 'thursday_end','friday_start', 'friday_end', 'saturday_start','saturday_end',
            'sunday_start','sunday_end')
admin.site.register(Docreg,docregadmin)
