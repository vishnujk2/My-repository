from django.contrib import admin
from . models import department,medical,Booked,Doctor

# Register your models here.
admin.site.register(department)
admin.site.register(medical)
admin.site.register(Doctor)

class Bookingadmin(admin.ModelAdmin):
    list_display = ('id','pat_name','pat_no','pat_email','Doc_name','booking_date','booked_on')
admin.site.register(Booked,Bookingadmin)