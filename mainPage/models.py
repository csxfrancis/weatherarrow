from django.db import models

# Create your models here.
class Forecast(models.Model):

    date = models.DateField()
    date_made = models.DateField()
    high = models.FloatField()
    low = models.FloatField()
    location = models.CharField(max_length=200)
    def getDate(self):
        print(self.date)
    def printInfo(self):


        print(self.date," ",self.location," - ",self.high,'-',self.low)
