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
        cities = ["garland","dallas","new york","houston","austin"]
        for cit in cities:
            apiKey = '130778f4cc0f6170a73e4baf0251a9f0'


            URL = 'http://api.openweathermap.org/data/2.5/forecast?q=' + cit + '&units=imperial'+'&appid=' + apiKey
            r = requests.get(URL)
            binary = r.content
            data = json.loads(binary)
            #print(data)
            max = 0
            min = 0
            prev = 0
            mxcast = 0
            mncast = 0
            for line in data["list"]:

                fcast = Forecast.objects.get_or_create(date = line["dt_txt"][0:10],date_made = today,temperature = line["main"]["temp"],feeltemp=line['main']['feels_like'],time_cast=line["dt_txt"][11:16],location = data["city"]["name"])[0]
                prev = fcast.date
                print(fcast.date)
                if(prev!=fcast.date):

                    max = fcast.temperature
                    min = fcast.temperature

                    mxcast.save()
                    mncast.save()
                else:
                    prev = fcast.date
                    if(fcast.temperature>max):
                        max = fcast.temperature
                        mxcast = fcast
                    elif(fcast.temperature<min):
                        min = fcast.temperature
                        mncast = fcast
                #fcast.printInfo()
                #fcast.save()

                #db.session.add(fcast)
            #db.session.commit()

    else:
        apiKey = '130778f4cc0f6170a73e4baf0251a9f0'

        URL = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=imperial'+'&appid=' + apiKey

        r = requests.get(URL)
        binary = r.content
        data = json.loads(binary)
        for line in data["list"]:
            fcast = Forecast.objects.get_or_create(date = line["dt_txt"][0:10],date_made = today,temperature = line["main"]["temp"],feeltemp=line['main']['feels_like'],time_cast=line["dt_txt"][11:16],location = data["city"]["name"])[0]
            #fcast.printInfo()
            #print(fcast.getDate())
            #fcast.save()

            #db.session.add(fcast)(value*(9/5) -459.67
        #db.session.commit()


if __name__ == "__main__":

    main()
