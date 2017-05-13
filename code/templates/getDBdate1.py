import sqlite3
import time as SYSTIME
from datetime import datetime
conn = sqlite3.connect('/home/pi/ELProj/ELProjmnt/envData.db')

date1 = '05/07/17'


def getData(datea):
    global dates
    global time
    global tempF
    global tempC
    global humid
    c = conn.cursor()

    #c.execute("select date from data where date between '{d1}'  and '{d2}'".\
      #  format(d1=datea, d2=dateb))
   # dates = c.fetchall()


    c.execute("select date from data where date = '{d1}'".\
        format(d1=datea))
    dates = c.fetchall()

    c.execute("select time from data where date = '{d1}'".\
        format(d1=datea))
    time = c.fetchall()

    c.execute("select tempF from data where date = '{d1}'".\
        format(d1=datea))
    tempF = c.fetchall()

    c.execute("select tempC from data where date = '{d1}'".\
        format(d1=datea))
    tempC = c.fetchall()

    c.execute("select humperC from data where date = '{d1}'".\
        format(d1=datea))
    humid = c.fetchall()


def getDates():
    return dates

def getTime():
    return time

def getTemp(tempType):
    if tempType == 1:
        return  tempF
    else:
        return  tempC

def getHumid():
    return humid

def getCurrent():
    global tempC
    global humid
    return tempC[-1], humid[-1] 

getData(date1)
newC, newHumid = getCurrent()
print newC
print newHumid
print dates
print time
print tempF
print tempC
print humid

    


