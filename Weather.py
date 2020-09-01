# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:10:41 2020

@author: Kianoush
"""


import pyowm
from win10toast import ToastNotifier 
import time

toaster = ToastNotifier() 


def weather ():
    owm = pyowm.OWM('your code from pyowm website')
    observation = owm.weather_at_place('Montreal,CA')
    w = observation.get_weather()
    
    temp = w.get_temperature('celsius')
    temp = str(temp['temp'])
    
    status = str(w.get_detailed_status())
    
    
    result = "Current Tempreture in Montreal: " + temp + "\n Currtent Status: " + status 
    toaster.show_toast("live Weather update", result, duration = 5,
                 icon_path="icon.ico", threaded=True) 


delay =  60 * 15  #     60 s * 15 min
now = time.time()
old = now
weather()

while now < old + delay:
    
    if now + 5 >= old + delay:
        old  = time.time()
        weather()
    now  = time.time()

    