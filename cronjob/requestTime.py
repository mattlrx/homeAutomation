#amsterdam Latitude and longitude coordinates are: 52.379189, 4.899431.

# https://api.sunrise-sunset.org/json?lat=52.378&lng=4.9&date=today

# response:
##{"results":{"sunrise":"3:19:53 AM","sunset":"8:06:50 PM","solar_noon":"11:43:22 AM","day_length":"16:46:57","civil_twilight_begin":"2:30:21 AM","civil_twilight_end":"8:56:22 PM","nautical_twilight_begin":"1:09:18 AM","nautical_twilight_end":"10:17:25 PM","astronomical_twilight_begin":"12:00:01 AM","astronomical_twilight_end":"12:00:01 AM"},"status":"OK"}

import requests
import json
import datetime
import pytz

# request the times for amsterdam for the current day
# returns the result object in json format
def getRequest():
    r = requests.get('https://api.sunrise-sunset.org/json?lat=52.378&lng=4.9&date=today')
    parsed_json=r.json()
    jsonResult=parsed_json['results']
    return jsonResult

def utcToLocaltime(timeStr):
    h,m,s = timeStr.split(':')
    if s.endswith('PM'):
        h= str(int(h)+12)
    my_date = datetime.datetime.now(pytz.timezone('Europe/Amsterdam'))
    offset = my_date.utcoffset()
    h = str(int(h) + int(str(offset).split(':')[0]))
    timeStr = h + ':' + m
    return timeStr

def getSunset():
    result = getRequest()
    sunsetTime = result['sunset']
    
    sunsetTime = utcToLocaltime(sunsetTime)
    
    return sunsetTime
    
def getSunrise():
    result = getRequest()
    sunriseTime = result['sunrise']
    sunriseTime = utcToLocaltime(sunriseTime)
    return sunriseTime

def getScheduleTime(timeName):
    result = getRequest()
    timeName = result[timeName]
    timeName = utcToLocaltime(timeName)
    return timeName




# print (getSunset())
# print (getSunrise())
# print (getScheduleTime('sunset'))