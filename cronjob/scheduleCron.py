#!/usr/bin/env python

from crontab import CronTab
import requestTime
import datetime
import sys

def createCreateCron():
    cron = CronTab(user='pi')
    cron.env['SHELL'] = '/bin/bash'
    cron.env['PATH'] = '/usr/bin:/bin'
    
    job = cron.new(command='python3 /home/pi/pythonproject/scheduleProject/scheduleCron.py sunrise', comment='createSunriseSchedule')
    job.minute.on(50)
    job.hour.on(17)
    cron.write()

def removeAllCron():
    cron = CronTab(user='pi')
    cron.remove_all()
    cron.write()

# jobName is sunset or sunrise
def getCommand(jobName):
    if jobName == 'sunset':
        command = 'python3 /home/pi/pythonproject/scheduleProject/remote.py allLightsOn'
    elif jobName == 'sunrise': 
        command = 'python3 /home/pi/pythonproject/scheduleProject/remote.py gardenLightOff'
    return command

# jobName is sunset or sunrise
def createCron(jobName):
    cron = CronTab(user='pi')
    hh,mm = requestTime.getScheduleTime(jobName).split(':')
    #remove existing job
    for job in cron:
        if job.comment == jobName:
            cron.remove(job)
            cron.write()

    job = cron.new(command=getCommand(jobName), comment=jobName)
    job.minute.on(int(mm))
    job.hour.on(int(hh))
    cron.write()
    print('done for '+ jobName)


def listCron():
    cron = CronTab(user='pi')
    for job in cron:
        print(job)



if str(sys.argv[1]) == 'createMain':
    createCreateCron()
elif str(sys.argv[1]) == 'sunrise':
    createCron('sunrise')
elif str(sys.argv[1]) == 'sunset':
    createCron('sunset')
elif str(sys.argv[1]) == 'list':
    print('list:')
    listCron()
elif str(sys.argv[1]) == 'removeAll':
    print('remove all jobs:')
    removeAllCron()
