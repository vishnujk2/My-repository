from django.db import models

# Create your models here.
class department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class medical(models.Model):
    driver_name = models.CharField(max_length=100)
    description = models.TextField()

class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.TextField()
    dep_name = models.ForeignKey(department, on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='vis')

    def __str__(self):
        return self.doc_name

class Booked(models.Model):
    pat_name = models.CharField(max_length=100)
    pat_no = models.CharField(max_length=10)
    pat_email = models.EmailField()
    Doc_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)