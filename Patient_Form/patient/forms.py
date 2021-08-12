from django import forms
from . models import Patient

class PatientForm(forms.ModelForm):
    CHOICE = (
        ('','Select option'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    Gender=forms.CharField(widget=forms.Select(choices=CHOICE))
    date=forms.CharField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    time=forms.CharField(widget=forms.TimeInput(attrs={'class':'timepicker'}))
    class Meta:
        model=Patient
        fields="__all__"

