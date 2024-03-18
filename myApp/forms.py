from django import forms
from myApp.models import *
from django.contrib.auth.forms import AuthenticationForm
from myApp.models import *
from .models import GovtEvent

class GovtEventForm(forms.ModelForm):
    class Meta:
        model = GovtEvent
        exclude = []  # Exclude all fields, as we are using widgets directly
        labels = {  # Empty dictionary to remove labels
            'date': '',
            'name': '',
            'parliament': '',
            'assembly': '',
            'venue': '',
            'pre_event_image': '',
            'mid_event_image': '',
            'post_event_image': '',
            'phone': '',
            'image': '',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'parliament': forms.Select(attrs={'class': 'form-control'}),
            'assembly': forms.Select(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Venue'}),
            'pre_event_image': forms.FileInput(attrs={'class': 'form-control'}),
            'mid_event_image': forms.FileInput(attrs={'class': 'form-control'}),
            'post_event_image': forms.FileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(GovtEventForm, self).__init__(*args, **kwargs)
        self.fields['parliament'].empty_label = 'Select Parliament'
        self.fields['assembly'].empty_label = 'Select Assembly'
