#!/usr/bin/env python

from crontab import CronTab
import requestTime
import datetime
import sys

def createCreateCron():
    cron = CronTab(user='matthieulrx')
    cron.env['SHELL'] = '/bin/bash'
    cron.env['PATH'] = '/usr/bin:/bin'
    
    job = cron.new(command='python3 /home/matthieulrx/_work/python/cronjob/scheduleCron.py sunset', comment='createMain')
    job.minute.on(00)
    job.hour.on(17)
    cron.write()

def removeAllCron():
    cron = CronTab(user='matthieulrx')
    cron.remove_all()
    cron.write()

# jobName is sunset or sunrise
def getCommand(jobName):
    if jobName == 'sunset':
        command = 'python3 /home/matthieulrx/_work/python/cronjob/lighton.py'
    elif jobName == 'sunrise': 
        command = 'python3 /home/matthieulrx/_work/python/cronjob/lightoff.py'
    return command

# jobName is sunset or sunrise
def createCron(jobName):
    cron = CronTab(user='matthieulrx')
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
    cron = CronTab(user='matthieulrx')
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