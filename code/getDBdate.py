import sqlite3
import time as SYSTIME
from datetime import datetime
#Using row factory allows us to access data not in tuple format
conn = sqlite3.connect('/home/pi/ELProj/ELProjmnt/envData.db', check_same_thread = False)
conn.row_factory=lambda cursor, row:row[0]

def getData(datea):
    global dates
    global time
    global tempF
    global tempC
    global humid
    d = conn.cursor()

    #This gives all the information from a row on a specific date and assigns it
    #to a variable
    dates = d.execute("select date from data where date = '{d1}'".\
        format(d1=datea)).fetchall()

    time = d.execute("select time from data where date = '{d1}'".\
        format(d1=datea)).fetchall()

    tempF = d.execute("select tempF from data where date = '{d1}'".\
        format(d1=datea)).fetchall()
    
    tempC = d.execute("select tempC from data where date = '{d1}'".\
        format(d1=datea)).fetchall()

    humid = d.execute("select humperC from data where date = '{d1}'".\
        format(d1=datea)).fetchall()

#Returns the variable
def getDates():
    return dates

def getTime():
    return time
#If passed 1 tempF is returned and any other is passed then TempC is returned
#this allows the user to specify which format they would like the temperature.
def getTemp(tempType):
    if tempType == 1:
        return  tempF
    else:
        return  tempC

def getHumid():
    return humid

#returning [-1] gives the most recent data recieved
def getCurrent():
    global tempC
    global humid
    return tempC[-1], humid[-1] 


    


