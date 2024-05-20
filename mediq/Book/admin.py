from django.contrib import admin
from Book.models import Book
class Bookadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','age','gender','hospital','doctor','message','phone')
admin.site.register(Book,Bookadmin)
