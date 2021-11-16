from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime 
from .models import Event

def all_events(request):
     event_list = Event.objects.all()
     return render(request, 
     'events/event_list.html',
     {
         'event_list':event_list,

     })

# Create your views here.
def home(request, year, month): #year=datetime.now.year, month=datetime.now.month
    name = "John"
    month = month.capitalize()
    #convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #create a calender
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)
    
    #get current year
    now = datetime.now()
    current_year = now.year

    #get current time
    time = now.strftime('%I:%M %p')
    return render(request,
            'events/home.html', {
            "name": name,
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal": cal,  
            "current_year" : current_year,
            "time" : time,
            })   