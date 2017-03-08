import os
import time
import sqlite3 as mydb
import sys

def readTemp():
  tempfile = open("/sys/bus/w1/devices/28-03168b11bbff/w1_slave")
  tempfile_text = tempfile.read()
  currentTime = time.strftime('%x %X %Z')
  tempfile.close()
  tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
  tempF = tempC*9.0/5.0+32.0
  return[currentTime, tempC, tempF]

def logTemp():
  for i in range(0,20):
    con = mydb.connect('templog.db')
    with con:
      try:
        [t,C,F]=readTemp()
        print "Current temperature is: %s F" %F
        cur = con.cursor()
        #sql = "insert into TempData values(?,?,?)"
        cur.execute('insert into TempData values(?,?,?)',(t,C,F))
        print "Temperature logged"
      except:
        print "Error!!"
      time.sleep(30)

#print readTemp()
logTemp()
