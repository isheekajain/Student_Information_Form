from django import forms
from django.forms import fields
from .models import Stud

class StudentForm(forms.ModelForm):
    class Meta:
        model = Stud
        fields = "__all__"