from django.shortcuts import render
from django.http import HttpResponse
from .models import department,medical,Doctor
from .forms import BookingForm
# Create your views here.

def main(request):
       return render(request,"home.html")

def about(request):
      return render(request,"about.html")

def booking(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
               form.save()
               return render(request,'confirm.html')
    form = BookingForm()
    dic_form={
        'xyz':form
        }
    return render(request,"booking.html",dic_form)

def contact(request):
        return render(request,"contact.html")

def departments(request):
        x={
                "dept": department.objects.all()
        }
        return render(request,"department.html",x)
        
def doctors(request):
        z={
                "doc": Doctor.objects.all()
        }
        return render(request,"doctors.html",z)




