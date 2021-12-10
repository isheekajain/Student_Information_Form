from django.forms.models import ModelForm
from django.shortcuts import render, redirect
from .models import Stud

from .form import StudentForm
#from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



def welcome(request):
    return render(request, "Welcome.html")

def load_form(request):
    form = StudentForm
    return render(request,"index.html", {'form' : form})

def add(request):
    form = StudentForm(request.POST)
    if form.is_valid():
     form.save()  
    return redirect('/show')


def show(request):
    student = Stud.objects.all
    return render(request, 'show.html', {'student' : student})    

def get_queryset(self, request):
    qs = super(ModelForm, self).get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(user=request.user)             

