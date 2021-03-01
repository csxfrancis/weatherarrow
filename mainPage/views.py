from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from mainPage.models import Forecast
from datetime import date
from django.views.generic import View





def timePlus(x):
    return str(x.date) + " " + str(x.time_cast)

def index(request):
    forecasts = Forecast.objects.order_by('location')
    forecast_list = {"forecasts":forecasts}
    return render(request,'mainPage/index.html',context=forecast_list)
def todayFilter(request):
        cday = date.today()

        if(request.method ==  "POST"):

            city = request.POST.get('city')
            forecasts = Forecast.objects.filter(location=city).filter(date=cday)

        else:
            forecasts = Forecast.objects.order_by('location').filter(date=cday)

        forecast_list = {"forecasts":forecasts}
        return render(request,'mainPage/today.html',forecast_list)
def today(request):
    check = False
    cday = date.today()
    if(request.method ==  "POST"):

        city = request.POST.get('city')
        print(city)
        #cday =  date.today()

        forecasts = Forecast.objects.filter(location=city).filter(date=cday).order_by('-date_made')

    else:
        city  = "Dallas"
        check = True
        forecasts = Forecast.objects.filter(location=city).filter(date=cday).order_by('-date_made')
    print(len(forecasts))
    if(len(forecasts)<8):
        cday = cday - timedelta(days=1)
        forecasts = Forecast.objects.filter(location=city).filter(date=cday).order_by('-date_made')

    top = forecasts.filter(date_made=cday)[0]
    forecast_list = {"forecasts":forecasts,"top":top,"check":check}
    return render(request,'mainPage/today.html',forecast_list)
def todayB(request):
    cday = date.today()

    forecasts = Forecast.objects.order_by('location').filter(date=cday).order_by('location')
    if(len(forecasts)<8):
        forecasts = Forecast.objects.filter(location=city).filter(date=cday.replace(cday-timedelta(days=1))).order_by('-date_made')

    forecast_list = {"forecasts":forecasts}
    return render(request,'mainPage/today.html',forecast_list)
def all(request):
    forecasts = Forecast.objects.order_by('location').order_by('-date')
    forecast_list = {"forecasts":forecasts}
    return render(request,'mainPage/all.html',context=forecast_list)
def compare(request):
    city = "Dallas"
    check = False
    cday = date.today()
    if(request.method ==  "POST"):
        check = True
        print('testing')
        city = request.POST.get('city')
        print(city)
    forecasts = Forecast.objects.filter(location=city).filter(date__gte=cday).order_by('date')

    keys = []
    coll = {}
    for cast in forecasts:
        #if cast.date in coll:
        #    temp = coll[cast.date]:
        key = cast.date
        kloc = cast.location
        if key in coll:
            temp = coll[key]
            temp.append(cast)
            coll[key] = temp
        else:
            keys.append(key)
            coll[key] = [cast]
    for x in keys:
        print(x)
    for n in coll:
        print(coll[n][0].location)

    forecast_list = {"forecasts":forecasts}
    return render(request,'mainPage/compare.html',context={'coll':coll,'check':check,'forecast_list':forecasts})

def history(request):
    city = "Dallas"
    check = False
    cday = date.today()
    if(request.method ==  "POST"):
        check = True
        print('testing')
        city = request.POST.get('city')
        print(city)
    forecasts = Forecast.objects.filter(location=city).filter(date__gte=cday).order_by('date')

    keys = []
    coll = {}
    for cast in forecasts:
        #if cast.date in coll:
        #    temp = coll[cast.date]:
        key = cast.date
        kloc = cast.location
        if key in coll:
            temp = coll[key]
            temp.append(cast)
            coll[key] = temp
        else:
            keys.append(key)
            coll[key] = [cast]
    for x in keys:
        print(x)
    for n in coll:
        print(coll[n][0].location)

    forecast_list = {"forecasts":forecasts}
    return render(request,'mainPage/compareV.html',context={'coll':coll,'check':check,'forecast_list':forecasts})
