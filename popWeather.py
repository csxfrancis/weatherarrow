import os

from datetime import date

import requests
import json
today = date.today()
os.environ.setdefault('DJANGO_SETTINGS_MODULE','weatherArrow.settings')
import django
django.setup()

import random
from mainPage.models import Forecast
def main():
    print("what city do you want?")
    city = input()

    if(city == "all"):
        cities = ["dallas","new york","houston","austin"]
        for cit in cities:
            apiKey = '130778f4cc0f6170a73e4baf0251a9f0'


            URL = 'http://api.openweathermap.org/data/2.5/forecast?q=' + cit + '&appid=' + apiKey
            r = requests.get(URL)
            binary = r.content
            data = json.loads(binary)
            for line in data["list"]:
                print(line)
                fcast = Forecast.objects.get_or_create(date = line["dt_txt"][0:10],date_made = today,temperature = line["main"]["temp"],time_cast=line["dt_txt"][11:16],location = data["city"]["name"])[0]

                fcast.save()

                #db.session.add(fcast)
            #db.session.commit()

    else:
        apiKey = '130778f4cc0f6170a73e4baf0251a9f0'


        URL = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=' + apiKey
        r = requests.get(URL)
        binary = r.content
        data = json.loads(binary)
        for line in data["list"]:
            fcast = Forecast.objects.get_or_create(date = line["dt_txt"][0:10],date_made = today,temperature = line["main"]["temp"],time_cast=line["dt_txt"][11:16],location = data["city"]["name"])[0]
            
            #print(fcast.getDate())
            fcast.save()

            #db.session.add(fcast)
        #db.session.commit()


if __name__ == "__main__":

    main()
