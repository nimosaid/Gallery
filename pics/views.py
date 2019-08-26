from django.shortcuts import render,redirect
import datetime as dt
from .models import Photo

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def pics_of_day(request):
    date = dt.date.today()
    return render(request, 'all-pics/today-pics.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def pics_today(request):
    date = dt.date.today()
    pics = Photo.todays_pics()
    return render(request, 'all-pics/today-pics.html', {"date": date,"pics":pics})

def search_results(request):

    if 'category' in request.GET and request.GET["Photo"]:
        search_term = request.GET.get("Photo")
        searched_photos = Photo.search_by_cat(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"photo": searched_photo})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})