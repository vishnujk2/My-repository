from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('about',views.about, name='about'),
    path('booking',views.booking,name='booking'),
    path('contact',views.contact,name='contact'),
    path('department',views.departments,name='department'),
    path('doctors',views.doctors,name='doctors'),
]
