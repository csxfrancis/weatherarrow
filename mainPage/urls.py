from django.contrib import admin
from django.urls import path
from mainPage import views

app_name = "mainPage"
urlpatterns = [
    path('',views.index),
    path('today/',views.today),
    path('todayS/',views.todayFilter,name="todayS"),
    path('todayF/',views.today,name="todayF"),
    path('compare/',views.compare,name='compare'),
    path('history/',views.history,name='history'),
    path('all/',views.all,name='all')


]
