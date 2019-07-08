from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import *
from .forms import *


def index(request,year=date.today().year,month=date.today().month): #year and month are added because of the urls.py int and str path converters
	year=int(year)
	month=int(month)
	if year < 1900 or year > 2099 : year=date.today().year
	month_name=calendar.month_name[month] #month_name func from the cal module to get month name that matches month number.
	cal=HTMLCalendar().formatmonth(year,month) #retrieve html formatted cal
	return render(request,'calendar_base.html',{'cal':cal})

def event(request):
	submitted=False
	if request.method=="POST":
		form=EventForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/event/?submitted=True')
	else:
	    form=EventForm()
	    if 'submitted' in request.GET:
	        submitted=True
	return render(request,'event.html',{'form':form,'submitted':submitted})  	

def all_events(request):
    events_list=Event.objects.all()
    return render(request,'all_events.html',{'events_list':events_list}) 


