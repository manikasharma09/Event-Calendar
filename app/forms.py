from django import forms
from django.forms import ModelForm
from .models import *

class EventForm(ModelForm):
	required_css_class='required'
	class Meta:
		model=Event
		fields ='__all__'		