from django.contrib import admin
from hospreg.models import Hospreg
class hospregadmin(admin.ModelAdmin):
    list_display=('hospital_name','hospital_type','email','phone','address','city','password','confirm_password','license','photo')
admin.site.register(Hospreg,hospregadmin)