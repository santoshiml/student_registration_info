from django import forms
from django.forms import ModelForm
from .models import STUDENT
class StudentForm(forms.ModelForm):
    class Meta:
        model = STUDENT
        fields = '__all__'
