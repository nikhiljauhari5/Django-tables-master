from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.
def home(request, year, month):
    #convert month from name to number
    month_number = list(calender.month_name).index(month)
    return render(request, 'home.html', 
        {
            "year": year,
            "month": month,
            "month_number": month_number,
        })