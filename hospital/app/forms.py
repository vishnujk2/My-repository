from django import forms
from . models import Booked

class Date(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booked
        fields='__all__'

        widgets={
            'booking_date': Date
        }
        labels = {
            'pat_name' : 'Name:',
            'pat_no' : 'Phone No:',
            'pat_email' : 'Email ID:',
            'Doc_name' :'Doctor Name',
            'booking_date' : "Booking date"
        }
