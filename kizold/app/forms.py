from django import forms
from django.forms import ModelForm, ValidationError
from .models import *


class BejegyzesForm(ModelForm):
    class Meta:
        model = Bejegyzes
        fields = ['osztaly_id', 'tevekenyseg_id']