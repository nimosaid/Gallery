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
# View Function to present pics from past days
def past_days_pics(request,past_date):
     try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

     except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False


        if date == dt.date.today():
            return redirect(pics_of_day)

        return render(request, 'all-pics/past-pics.html', {"date": date,"pics":pics})

def pics_today(request):
    date = dt.date.today()
    news = Photo.todays_pics()
    return render(request, 'all-pics/today-pics.html', {"date": date,"pics":pics})

def search_results(request):

    if 'photo' in request.GET and request.GET["Photo"]:
        search_term = request.GET.get("Photo")
        searched_articles = Photo.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"photos": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})