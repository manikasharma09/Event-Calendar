from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

def index(request,year,month): #year and month are added because of the urls.py int and str path converters
	year=int(year)
	month=int(month)
	if year < 1900 or year > 2099 : year=date.today().year
	month_name=calendar.month_name[month] #month_name func from the cal module to get month name that matches month number.
	title="My Event Ananya Calendar - %s %s" % (month_name,year)
	cal=HTMLCalendar().formatmonth(year,month) #retrieve html formatted cal
	return render(request,'base.html',{'title':title,'cal':cal})
