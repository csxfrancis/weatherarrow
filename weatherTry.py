import os

from datetime import date, timedelta

import requests
import json
today = date.today()
os.environ.setdefault('DJANGO_SETTINGS_MODULE','weatherArrow.settings')
import django
django.setup()

import random
from mainPage.models import Forecast
apiKey = '130778f4cc0f6170a73e4baf0251a9f0'


os.environ.setdefault('DJANGO_SETTINGS_MODULE','weatherArrow.settings')



codes = [['Dallas',32.7767,-96.797],['Houston',29.7604,-95.3698],['New York City',40.7128,-74.0060],['Miami',25.7617,-80.1918],['Los Angeles',34.0522,-118.2437],['Seattle',47.6062,-122.3321]]

max = 0
min = 0
prev = 0
mxcast = 0
mncast = 0

for city,lat,lon in codes:
    #URL='https://api.openweathermap.org/data/2.5/onecall?lat=32.7&lon=-96.7&appid=130778f4cc0f6170a73e4baf0251a9f0'
    print(city,lat,lon)
    cur = date.today()
    URL = 'https://api.openweathermap.org/data/2.5/onecall?lat='+str(lat)+'&lon='+str(lon)+'&units=imperial'+'&appid='+apiKey
    print(URL)
    r = requests.get(URL)
    binary = r.content
    data = json.loads(binary)
    #print(data)
    #print(city)
    for line in data['daily']:
        print(len(data['daily']))
        print(line["dt"])

        fcast = Forecast.objects.get_or_create(date = cur,date_made = today,high= line["temp"]["max"],low=line["temp"]['min'],location = city)[0]
        fcast.printInfo()
        fcast.save()
        cur = cur + timedelta(days=1)


#for line in data["list"]:

    #fcast = Forecast.objects.get_or_create(date = line["dt_txt"][0:10],date_made = today,temperature = line["main"]["temp"],feeltemp=line['main']['feels_like'],time_cast=line["dt_txt"][11:16],location = data["city"]["name"])[0]

    #fcast.printInfo()
    #fcast.save()

    #db.session.add(fcast)
#db.session.commit()
